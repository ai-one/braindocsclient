#!/usr/bin/env python
""" Copyright (c) 2015 ai-one inc., La Jolla CA. All rights reserved.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Sequence, UnicodeText, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref 
from contextlib import contextmanager

Base = declarative_base()

class AnalysisResultTextUnit(Base):
    __tablename__ = 'analysisresults_textunit'
    _id = Column(String(32), primary_key=True)
    score = Column(Float)
    fingerprint_id = Column(Integer())
    similarityAnalysis_id = Column(String(32), ForeignKey('analysisresults.analysisId'))
    doc_id = Column(String(32))
    doc_name = Column(UnicodeText())
    relevancy = Column(String(45))
    agentId = Column(String(32))
    agentName = Column(UnicodeText())
    text_unit_ids = Column(String(32))
    text = Column(UnicodeText())

    def __repr__(self):
        return "<AnalysisResultTextUnit(_id='%s', score=%s, fingerprint_id=%s, ..., text=%s)>" % (
            self._id, self.score, self.fingerprint_id, 
            self.text if self.text is None or len(self.text) < 10 else self.text[:10] + "...")

class AnalysisResult(Base):
    __tablename__ = 'analysisresults'
    _id = Column(String(32))
    analysisId = Column(String(32), primary_key=True)
    textunits = relationship("AnalysisResultTextUnit", order_by=AnalysisResultTextUnit.score.desc(), backref=backref('analysis'))
    agentBaselineScore = Column(Float())
    agentId = Column(String(32))
    agentLibraryId = Column(String(32))
    agentName = Column(UnicodeText())
    create_date = Column(DateTime())
    customKeywordBoost = Column(String(32))
    customKeywords = Column(UnicodeText())
    cutoffScore = Column(String(32))
    handleWindow = Column(String(32))
    libraryId = Column(String(32))
    libraryName = Column(UnicodeText())
    name = Column(UnicodeText())
    status = Column(String(32))
    userid = Column(String(32))
    def __repr__(self):
        textunits = ""
        if len(self.textunits) >= 1:
            textunits = repr(self.textunits)
        if len(self.textunits) > 1:
            textunits += ", ..."
        return "<AnalysisResult(_id='%s', name=%s, textunits=[%s], libraryName=%s, agentName=%s, ...)>" % (
            self._id, self.name, textunits, self.libraryName, self.agentName)

@contextmanager
def session_scope(session):
    """Provide a transactional scope around a series of operations."""
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()