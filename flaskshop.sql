-- phpMyAdmin SQL Dump
-- version phpStudy 2014
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2018 年 08 月 31 日 11:32
-- 服务器版本: 5.5.53
-- PHP 版本: 5.4.45

--
-- 数据库: `flask`
--

-- --------------------------------------------------------

--
-- 表的结构 `goods`
--

CREATE TABLE IF NOT EXISTS `goods` (
  `gid` varchar(10) NOT NULL DEFAULT '',
  `pic` varchar(10) DEFAULT NULL,
  `introduction` varchar(100) DEFAULT NULL,
  `price` double DEFAULT NULL,
  `gname` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`gid`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `goods`
--

INSERT INTO `goods` (`gid`, `pic`, `introduction`, `price`, `gname`) VALUES
('1', '1.jpg', 'CPU品牌:Apple/苹果<br>Apple型号:iPhone X<br>机身颜色：银色 深空灰色', 6666, 'iPhone X'),
('2', '2.jpg', 'Apple/苹果 13英寸：MacBook Pro 128GB轻薄学生商务办公I5超薄电脑', 8888, 'MacBook Pro'),
('3', '3.jpg', '智能双GPS定位 返航 专业无人机 高清航拍 遥控飞机4K四轴飞行器', 777, '智能专业遥控无人机'),
('4', '4.jpg', '秋季潮牌韩版潮流 宽松ins长袖T恤 男嘻哈运动衣服 套头bf风 休闲上衣', 88, 'ins 最火长袖T恤'),
('5', '5.jpg', '【限量100套】MAC/魅可迷你唇膏套组5支装 mini口红套装礼物chili ', 520, 'MAC mini口红套装礼物chili'),
('6', '6.jpg', '专柜正品耐克Air Jordan 11 UNC AJ11乔11午夜蓝高帮篮球鞋378037 ', 998, 'Nike AJ11');

-- --------------------------------------------------------

--
-- 表的结构 `history`
--

CREATE TABLE IF NOT EXISTS `history` (
  `telphone` varchar(11) DEFAULT NULL,
  `gid` int(11) NOT NULL,
  `datetime` datetime DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `history`
--

INSERT INTO `history` (`telphone`, `gid`, `datetime`) VALUES
('110', 1, '2018-08-31 19:20:45');

-- --------------------------------------------------------

--
-- 表的结构 `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `telephone` varchar(11) NOT NULL DEFAULT '',
  `username` varchar(20) NOT NULL,
  `password` varchar(32) NOT NULL,
  `money` float DEFAULT NULL,
  PRIMARY KEY (`telephone`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `users`
--

INSERT INTO `users` (`telephone`, `username`, `password`, `money`) VALUES
('110', 'olivia', '698d51a19d8a121ce581499d7b701668', 9996770),
('178', 'v0w', '698d51a19d8a121ce581499d7b701668', 0);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
