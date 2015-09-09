CREATE TABLE `analysisresults_textunit` (
  `_id` varchar(12) NOT NULL,
  `score` float DEFAULT NULL,
  `fingerprint_id` int(11) DEFAULT NULL,
  `similarityAnalysis_id` varchar(15) DEFAULT NULL,
  `doc_id` varchar(12) DEFAULT NULL,
  `doc_name` longtext,
  `relevancy` varchar(45) DEFAULT NULL,
  `agentId` varchar(12) DEFAULT NULL,
  `agentName` longtext,
  `text_unit_ids` varchar(12) DEFAULT NULL,
  `text` longtext,
  PRIMARY KEY (`_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;