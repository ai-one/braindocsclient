#!/usr/bin/env python
""" Copyright (c) 2015 ai-one inc., La Jolla CA. All rights reserved.
"""

from __future__ import print_function
import dateutil.parser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from bdAPI import bdAPI
from database import Base, AnalysisResult, AnalysisResultTextUnit, session_scope
from configparser import PromptingConfigParser, promptyesno

def iterprogress(it, name="task", freq=10, total=None):
    if total is None:
        try:
            total = len(it)
        except:
            pass
    for idx, item in enumerate(it):
        if idx % freq == 0:
            if not total is None:
                print("%s: processed %s of %s ..." % (name, idx+1, total))
            else:
                print("%s: processed %s ..." % (name, idx+1))
        yield item
    print("%s: done" % name)

def main():
    """ Prompt user & initialization
    """

    print("braindocs2database")
    print("Copyright (c) 2015 ai-one inc. All rights reserved.")
    print("")
    print(">>> Current settings:\n")

    cfg = PromptingConfigParser()

    # add default settings
    cfg.add_section("braindocs")
    cfg.add_section("database")
    cfg.set("database", "url", "mysql://root@localhost/braindocs")
    cfg.set("braindocs", "username", "bd_user")
    cfg.set("braindocs", "password", "bd_pw")
    cfg.set("braindocs", "url", "https://nathandev2.cloudapp.net/at")

    # read settings from file
    cfg.read("braindocs2database.config")

    # prompt update
    print(cfg)
    while promptyesno("\nUpdate settings?"):
        print("")
        cfg.prompt()
        with open("braindocs2database.config", 'wb') as fp:
            cfg.write(fp)
        print("\n>>> Updated settings:\n")
        print(cfg)
    
    """ Setup database connection
    """

    engine = create_engine(cfg.get("database", "url"), echo=False)

    #Base.metadata.drop_all(engine) # optional: drop all
    Base.metadata.create_all(engine)
 
    Session = sessionmaker(bind=engine)

    """ Setup braindocs connection
    """

    bd = bdAPI(
        username=cfg.get("braindocs", "username"),
        password=cfg.get("braindocs", "password"),
        baseURL=cfg.get("braindocs", "url"))

    """ Import braindocs entries into database
    """

    print("\nStarting import...")
    with session_scope(Session()) as session:
        for ar in iterprogress(bd.getAnalysisResults(), "importing analysis results", 1):
            arentry = AnalysisResult()
            for key, value in ar.iteritems():
                if key in ["customKeywords", "userid"]:
                    if not value is None: 
                        value = ",".join(v.replace(",", "\\,") for v in value)
                if key == "create_date":
                    value = dateutil.parser.parse(value).replace(tzinfo=None)
                setattr(arentry, key, value)
                if key == "analysisId":
                    for tu in bd.getAnalysisDetailsTextUnits(value):
                        tuentry = AnalysisResultTextUnit()
                        for key, value in tu.iteritems():
                            setattr(tuentry, key, value)
                        arentry.textunits.append(tuentry)
            session.merge(arentry)

if __name__ == "__main__":
    main()