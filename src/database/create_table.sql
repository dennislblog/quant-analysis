SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

CREATE TABLE `history` (
  `id` int(11) NOT NULL,
  `stock_id` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `opening` decimal(12,2) NOT NULL DEFAULT '0.00',
  `closing` decimal(12,2) NOT NULL DEFAULT '0.00',
  `difference` decimal(12,2) NOT NULL DEFAULT '0.00' COMMENT 'day-to-day differences',
  `percentage_difference` decimal(12,2) NOT NULL DEFAULT '0.00',
  `lowest` decimal(12,2) NOT NULL DEFAULT '0.00',
  `highest` decimal(12,2) NOT NULL DEFAULT '0.00',
  `volume` int(11) NOT NULL DEFAULT '0',
  `amount` decimal(20,2) NOT NULL DEFAULT '0.00' COMMENT 'transaction/10000'
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='Historical Table';


CREATE TABLE `stock` (
  `id` int(11) NOT NULL COMMENT 'Stock ID',
  `name` varchar(100) NOT NULL COMMENT 'Stock Name',
  `code` varchar(30) NOT NULL COMMENT 'Stock Country'
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='Stock Table';
