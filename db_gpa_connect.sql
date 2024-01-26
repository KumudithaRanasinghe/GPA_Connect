-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 24, 2024 at 06:51 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_gpa_connect`
--

-- --------------------------------------------------------

--
-- Table structure for table `degree`
--

CREATE TABLE `degree` (
  `d_id` int(11) NOT NULL,
  `d_name` varchar(50) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `degree`
--

INSERT INTO `degree` (`d_id`, `d_name`) VALUES
(1, 'BSc (Hons) in Computer Science  '),
(2, 'BSc (Honours) in Data Science  '),
(3, 'BSc (Hons) in Software Engineering'),
(4, 'BSc in Management Information Systems (Special)');

-- --------------------------------------------------------

--
-- Table structure for table `degree_module`
--

CREATE TABLE `degree_module` (
  `d_id` int(11) NOT NULL,
  `m_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `degree_module`
--

INSERT INTO `degree_module` (`d_id`, `m_id`) VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(1, 5),
(1, 6),
(1, 7),
(1, 8),
(1, 9),
(1, 10),
(1, 11),
(1, 12),
(1, 13),
(1, 14),
(1, 15),
(1, 16),
(1, 17),
(1, 18),
(1, 19),
(1, 20),
(1, 21),
(1, 27),
(1, 29),
(1, 30),
(1, 31),
(1, 32),
(1, 33),
(1, 34),
(1, 35),
(1, 36),
(1, 37),
(1, 37),
(1, 38),
(1, 39),
(1, 40),
(1, 40),
(1, 41),
(1, 42),
(1, 43),
(1, 44),
(1, 45),
(1, 46),
(1, 47),
(1, 49),
(1, 50),
(1, 51),
(2, 1),
(2, 2),
(2, 3),
(2, 4),
(2, 4),
(2, 5),
(2, 6),
(2, 7),
(2, 8),
(2, 9),
(2, 10),
(2, 57),
(2, 15),
(2, 58),
(2, 59),
(2, 17),
(2, 14),
(2, 60),
(2, 19),
(2, 61),
(2, 62),
(2, 63),
(2, 64),
(2, 45),
(2, 68),
(2, 34),
(2, 27),
(2, 21),
(2, 65),
(2, 66),
(2, 36),
(2, 67),
(2, 69),
(2, 70),
(2, 71),
(2, 72),
(2, 73),
(2, 41),
(2, 74),
(2, 75),
(2, 44),
(2, 46),
(2, 40),
(3, 1),
(3, 2),
(3, 3),
(3, 5),
(3, 6),
(3, 7),
(3, 8),
(3, 9),
(3, 10),
(3, 11),
(3, 12),
(3, 13),
(3, 14),
(3, 15),
(3, 16),
(3, 17),
(3, 18),
(3, 19),
(3, 20),
(3, 21),
(3, 27),
(3, 29),
(3, 85),
(3, 31),
(3, 34),
(3, 36),
(3, 37),
(3, 53),
(3, 54),
(3, 47),
(3, 45),
(3, 86),
(3, 38),
(3, 55),
(3, 56),
(3, 49),
(3, 82),
(3, 40),
(3, 43),
(3, 41),
(3, 44),
(3, 42),
(4, 1),
(4, 2),
(4, 3),
(4, 4),
(4, 5),
(4, 5),
(4, 6),
(4, 7),
(0, 8),
(4, 7),
(4, 8),
(4, 9),
(4, 10),
(4, 11),
(4, 12),
(4, 13),
(4, 14),
(4, 15),
(4, 16),
(4, 17),
(4, 18),
(4, 19),
(4, 20),
(4, 21),
(4, 27),
(4, 29),
(4, 30),
(4, 53),
(4, 77),
(4, 34),
(4, 78),
(4, 79),
(4, 36),
(4, 37),
(4, 81),
(4, 47),
(4, 45),
(4, 86),
(4, 38),
(4, 80),
(4, 56),
(4, 49),
(4, 39),
(4, 82),
(4, 40),
(4, 83),
(4, 84),
(3, 4);

-- --------------------------------------------------------

--
-- Table structure for table `grade`
--

CREATE TABLE `grade` (
  `g_id` int(11) NOT NULL,
  `g_symbol` varchar(50) NOT NULL,
  `g_point` float NOT NULL,
  `marks_range` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `grade`
--

INSERT INTO `grade` (`g_id`, `g_symbol`, `g_point`, `marks_range`) VALUES
(1, 'F', 0, '0-24'),
(2, 'D', 1, '25-29'),
(3, 'D+', 1.3, '30-34'),
(4, 'C-', 1.7, '35-39'),
(5, 'C', 2, '40-44'),
(6, 'C+', 2.3, '45-49'),
(7, 'B-', 2.7, '50-54'),
(8, 'B', 3, '55-59'),
(9, 'B+', 3.3, '60-64'),
(10, 'A-', 3.7, '65-69'),
(11, 'A', 4, '70-84'),
(12, 'A+', 4, '85-100');

-- --------------------------------------------------------

--
-- Table structure for table `module`
--

CREATE TABLE `module` (
  `m_id` int(11) NOT NULL,
  `m_name` varchar(100) NOT NULL,
  `m_credits` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `module`
--

INSERT INTO `module` (`m_id`, `m_name`, `m_credits`) VALUES
(1, 'Introduction to Computer Science', 3),
(2, 'Mathematics for Computing', 3),
(3, 'Programming in C', 3),
(4, 'Professional Development', 3),
(5, 'Data communications and networks', 3),
(6, 'Object Oriented Programming with Java', 3),
(7, 'Algorithms and Data Structures', 3),
(8, 'Computer Architecture', 3),
(9, 'Database Management Systems', 3),
(10, 'Web Based Application Development', 3),
(11, 'Computer Networks', 3),
(12, 'Systems Analysis and Design', 3),
(13, 'Statistics for Computing', 3),
(14, 'Development of Enterprise Applications I', 3),
(15, 'Human-Computer Interaction', 3),
(16, 'Business Processes and ERP', 3),
(17, 'Introduction to Software Engineering', 3),
(18, 'Software Architecture', 3),
(19, 'Algorithms and Complexity', 3),
(20, 'Operating Systems', 3),
(21, 'Internship', 3),
(27, 'Information Assurance and Security', 3),
(29, 'Social Issues and Professional Practice', 3),
(30, 'Wireless Technologies and Network Programming', 3),
(31, 'Advanced Mathematics for Computing\r\n', 3),
(32, 'Computational Theory', 3),
(33, 'Programming Languages and Compiler Design', 3),
(34, 'Advanced Database Management Systems', 3),
(35, 'Cryptography', 3),
(36, 'Mobile Application Development', 3),
(37, 'Software Process Management', 3),
(38, 'Business Policy and Strategy', 3),
(39, 'Entrepreneurship', 3),
(40, 'Development of Enterprise Applications II', 3),
(41, 'Artificial Intelligence', 3),
(42, 'Embedded Systems', 3),
(43, 'Computer Graphics and Visualization', 3),
(44, 'Parallel and Distributed Computing', 3),
(45, 'Data Warehousing and Data Mining', 3),
(46, 'Internet of Things', 3),
(47, ' Platform Based Development', 3),
(49, 'Agent Based Systems', 3),
(50, 'CS Honours Award Project', 3),
(51, 'Bio Informatics', 3),
(52, 'Software Verification and Validation', 3),
(53, 'IT Project Management', 3),
(54, 'SE Honours Award Project', 3),
(55, 'Enterprise Networks', 3),
(56, 'E-Business Application Development', 3),
(57, 'Introduction to Data Science', 3),
(58, 'Data Programming with R', 3),
(59, 'Statistics for Data Science', 3),
(60, 'System Fundamentals', 3),
(61, 'Data Science in Python', 3),
(62, 'Ethics in Data Science', 3),
(63, 'Web Mining', 3),
(64, 'Advanced Statistics for Data Science\r\n', 3),
(65, 'Cloud Computing', 3),
(66, 'Machine Learning', 3),
(67, 'Big Data Analytics\r\n', 3),
(68, 'Data Visualization\r\n', 3),
(69, 'Natural Language Processing\r\n', 3),
(70, 'Neural Networks\r\n', 3),
(71, 'Big Data Programming\r\n', 3),
(72, 'DS Honors Award Project\r\n', 3),
(73, 'Urban Computing\r\n', 3),
(74, 'Data Science Trends and Applications\r\n', 3),
(75, 'Deep Learning\r\n', 3),
(76, 'IT Project Management\r\n', 3),
(77, 'IT Audit and Control\r\n', 3),
(78, 'Enterprise Architecture\r\n', 3),
(79, 'Software Quality Assurance\r\n', 3),
(80, 'Enterprise Networks\r\n', 3),
(81, 'MIS Special Award Project\r\n', 3),
(82, 'Management Information Systems\r\n', 3),
(83, 'Disaster Recovery and High availability Techniques\r\n', 3),
(84, 'Business Analytics', 3),
(85, 'Software Verification and Validation', 3),
(86, 'Internet of Things', 3);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `u_id` int(11) NOT NULL,
  `u_name` varchar(255) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(150) NOT NULL,
  `gpa` float NOT NULL,
  `d_id` int(11) NOT NULL,
  `user_type` varchar(10) NOT NULL,
  `u_password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`u_id`, `u_name`, `name`, `email`, `gpa`, `d_id`, `user_type`, `u_password`) VALUES
(28230, 'Saman12', 'saman kumara', 'saman123@gmail.com', 0, 0, 'student', 'pbkdf2:sha256:600000$wfukpEIu$9aeff93714e0d6650216d3466cf4c8e4907597dce4c89165ed23caf73ca827c1'),
(28232, 'dushan6693', 'dushan', 'saman123@gmail.com', 0, 0, 'student', 'pbkdf2:sha256:600000$vjkgGV84$b9b96b76f3ed71da175551ce9269113c619f196cb39629d1a9a1e5a2c7e41dcf'),
(28236, 'admin', '', 'admin123@nsbm.lk', 0, 0, 'admin', 'pbkdf2:sha256:600000$I1bfiXWr$e78c975b869433d8e93f624f598c6fa3ca0c12e354dd3c2511c438123531c820');

-- --------------------------------------------------------

--
-- Table structure for table `user_module_grade`
--

CREATE TABLE `user_module_grade` (
  `s_m_g_id` int(11) NOT NULL,
  `s_id` int(11) NOT NULL,
  `m_id` int(11) NOT NULL,
  `g_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_module_grade`
--

INSERT INTO `user_module_grade` (`s_m_g_id`, `s_id`, `m_id`, `g_id`) VALUES
(1, 28232, 1, 6),
(2, 28230, 2, 7);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `degree`
--
ALTER TABLE `degree`
  ADD PRIMARY KEY (`d_id`);

--
-- Indexes for table `degree_module`
--
ALTER TABLE `degree_module`
  ADD KEY `DD` (`d_id`),
  ADD KEY `DDF` (`m_id`);

--
-- Indexes for table `grade`
--
ALTER TABLE `grade`
  ADD PRIMARY KEY (`g_id`);

--
-- Indexes for table `module`
--
ALTER TABLE `module`
  ADD PRIMARY KEY (`m_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`u_id`);

--
-- Indexes for table `user_module_grade`
--
ALTER TABLE `user_module_grade`
  ADD PRIMARY KEY (`s_m_g_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `degree`
--
ALTER TABLE `degree`
  MODIFY `d_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `grade`
--
ALTER TABLE `grade`
  MODIFY `g_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `module`
--
ALTER TABLE `module`
  MODIFY `m_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=87;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `u_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=94301;

--
-- AUTO_INCREMENT for table `user_module_grade`
--
ALTER TABLE `user_module_grade`
  MODIFY `s_m_g_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `degree_module`
--
ALTER TABLE `degree_module`
  ADD CONSTRAINT `degree_module_ibfk_1` FOREIGN KEY (`m_id`) REFERENCES `module` (`m_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
