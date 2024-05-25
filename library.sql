-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 18, 2020 at 09:15 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library`
--

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `book_id` int(11) NOT NULL,
  `title` varchar(70) DEFAULT NULL,
  `author` varchar(50) DEFAULT NULL,
  `pages` int(11) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `publisher` varchar(20) DEFAULT NULL,
  `book_type` varchar(20) DEFAULT NULL,
  `book_status` int(11) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`book_id`, `title`, `author`, `pages`, `price`, `publisher`, `book_type`, `book_status`) VALUES
(1, 'c programing', 'Dennis Ritchie', 600, 800, 'textmaz', 'Reference', 1),
(2, 'C: the Complete Reference', 'Schildt Herbert', 832, 500, 'McGraw Hill India', 'Reference', 0),
(3, 'C: The Complete Reference', 'SCHILDT and HERBERT, McGraw Hill', 832, 652, ' McGraw Hill', 'Reference', 0),
(4, 'PHP & MySQL Novice to Ninja', 'Tom Butler & Kevin Yank', 450, 700, 'SitePoint', 'Reference', 0),
(5, 'Head First PHP & MySQL', 'Lynn Beighley & Michael Morrison', 812, 1000, 'O’Reilly', 'Reference', 0),
(6, 'Programming PHP: Creating Dynamic Web Pages', 'Kevin Tatroe, Peter MacIntyre & Rasmus Lerdorf For', 550, 700, '`O’Reilly', 'Reference', 0),
(7, 'Java - The Complete Reference', 'Herbert Schildt', 500, 1000, 'N/A', 'Reference', 0),
(8, 'Python Crash Course', 'Eric Matthews', 560, 700, 'N/A', 'Reference', 0),
(9, 'Head-First Python (2nd edition)', 'Paul Barry', 445, 700, 'N/A', 'Reference', 0),
(10, 'Modern Full-Stack Development', 'Webpack, and Docker', 400, 700, 'N/A', 'REFERENCE', 0),
(11, 'Hands-On JavaScript High Performance', 'Justin Scherer', 400, 600, 'N/A', 'Reference', 0),
(12, 'JavaScript Everywhere', 'Adam D. Scott', 322, 400, 'N/A', 'Reference', 0),
(13, 'Web Development with Node and Express', 'Ethan Brown', 420, 500, 'N/A', 'Reference', 0),
(14, 'Professional JavaScript', 'Hugo Di Francesco, Siyuan Gao, Vinicius Isola', 420, 500, 'N/A', 'REFERENCE', 0),
(15, 'Jurassic Park', 'Michael Crichton', 466, 700, 'Ballantine Books', 'Action and adventure', 0),
(16, 'The Hobbit', 'J.R.R. Tolkien', 366, 100, 'Houghton Mifflin', 'Action and adventure', 0),
(17, 'A Game of Thrones', 'George R.R. Martin', 819, 800, 'Bantam ', 'Action and adventure', 0),
(18, 'History of Modern Art: Painting Sculpture Architec', 'H. Harvard Arnason, Peter R. Kalb', 832, 500, 'Prentice Hall ', 'Art/architecture', 0),
(19, 'History of Italian Renaissance Art: Painting, Scul', 'Frederick Hartt, David G. Wilkins', 704, 600, 'Prentice Hall', 'Art/architecture', 0),
(20, 'Making: Anthropology, Archaeology, Art and Archite', 'Tim Ingold', 162, 100, 'Routledge ', 'Art/architecture', 0),
(21, 'The Best Alternate History Stories of the 20th Cen', 'Harry Turtledove', 415, 300, 'Del Rey', 'Alternate history', 0),
(22, 'From the Ashes: An Alternate History Novel', 'Sandra Saidak', 388, 400, 'Uffington Horse Pres', 'Alternate history', 0),
(23, 'The Mammoth Book of Alternate Histories', 'Ian Watson', 591, 600, 'Robinson Publishing', 'Alternate history', 0),
(24, 'Gandhi: An autobiography', 'Mahatma Gandhi and Mahadev Desai', 528, 700, 'Beacon Press', 'Autobiography', 0),
(25, 'The Autobiography of Benjamin Franklin', 'Benjamin Franklin', 142, 200, 'Touchstone ', 'Autobiography', 0),
(26, 'Boy: Tales of Childhood', 'Roald Dahl, and Quentin Blake', 176, 220, 'Puffin Books', 'Autobiography', 0),
(27, 'Jerusalem: The Biography', 'Simon Sebag Montefiore', 752, 800, 'Weidenfeld & Nicolso', 'Biography', 0),
(28, 'London: The Biography', 'Peter Ackroyd', 801, 900, 'Anchor Books ', 'Biography', 0),
(29, 'Victoria The Queen', 'Julia Baird', 696, 800, 'Random House', 'Biography', 0),
(30, 'IIM Ahmedabad Business Books: Day to Day Economics', 'Satish Y. Deodhar', 232, 300, 'Random House India', 'Business/economics', 0),
(31, 'Student Solutions Manual for Statistics for Busine', 'Paul Newbold, William Carlson, Betty M. Thorne', 304, 500, 'Pearson ', 'Business/economics', 0),
(32, 'Statistics for Business and Economics [with Studen', 'Paul Newbold, William Carlson, William L. Carlson,', 1016, 1500, 'Prentice Hall', 'Business/economics', 0),
(33, 'Craft, Inc.: Turn Your Creative Hobby into a Business', 'Meg Mateo Ilasco', 160, 250, 'Chronicle Books', 'Crafts/hobbies', 0),
(34, 'Crafts and hobbies', 'Daniel Weiss, Reader\'s Digest Association, Susan C', 456, 600, 'Readers Digest', 'Crafts/hobbies', 0),
(35, 'Crochet: Amazing Crochet Patterns To Take You From Beginner to Interme', 'Emma Scott', 67, 200, 'B00WCCKRMA', 'Crafts/hobbies', 0),
(36, 'The Smitten Kitchen Cookbook', 'Deb Perelman', 336, 500, 'Knopf', 'Cookbook', 0),
(37, 'The Barefoot Contessa Cookbook', 'Ina Garten, Melanie Acevedo', 256, 400, 'Clarkson Potter', 'Cookbook', 0),
(38, 'Betty Crocker\'s Cookbook', 'Betty Crocker', 575, 800, ' Golden Books', 'Cookbook', 0),
(39, 'Comic Book for Blood of Olympus', 'Blue Books', 9, 120, 'N/A', 'Comic book', 0),
(40, 'Star Wars', ' Miles Lane, Nicola Scott (Illustrator), Nicola Sc', 24, 100, 'Marvel', 'Comic book', 0),
(41, 'A Game of Thrones', 'Daniel Abraham (Adaptation), George R.R. Martin, T', 46, 200, 'Dynamite Entertainme', 'Comic book', 0),
(42, 'The Encyclopedia of Early Earth', 'Isabel Greenberg', 176, 250, 'Bond Street Books', 'Encyclopedia', 0),
(43, 'Encyclopedia of an Ordinary Life', 'Amy Krouse Rosenthal', 240, 300, 'Broadway Books', 'Encyclopedia', 0),
(44, 'The Encyclopedia of Country Living', 'Carla Emery', 922, 1500, 'Sasquatch Books', 'Encyclopedia', 0),
(45, 'Drama', 'Raina Telgemeier', 238, 400, 'Graphix', 'Drama', 0),
(46, 'Are You My Mother? A Comic Drama', 'Alison Bechdel', 290, 500, 'Houghton Mifflin', 'Drama', 0),
(47, 'The Fight', 'L. Divine', 202, 250, 'Dafina Books', 'Drama', 0),
(48, 'The Big Book of Health and Fitness', 'Philip Maffetone', 544, 700, 'Skyhorse Publishing', 'Health/fitness', 0),
(49, 'Live Young Forever: 12 Steps to Optimum Health, Fitness & Longevity', 'Jack LaLanne', 288, 350, 'Robert Kennedy Publi', 'Health/fitness', 0),
(50, 'A Brief History of Time', ' Stephen Hawking', 212, 800, 'Bantam Books', 'Science fiction', 0),
(51, 'The Big Book of Science Fiction', 'Ann VanderMeer', 1178, 2000, 'Vintage', 'Science fiction', 0),
(52, 'The Enceladus Mission: Hard Science Fiction', 'Brandon Q. Morris', 436, 500, 'Hard-SF.com', 'Science fiction', 0),
(53, 'The Hobbit: Graphic Novel', 'Chuck Dixon', 133, 500, 'Ballantine Books', 'Graphic novel', 0),
(54, 'The Legend of Sleepy Hollow (Graphic Novel)', 'Bo Hampton', 64, 200, 'Image Comics', 'Graphic novel', 0),
(55, 'A Wrinkle in Time: The Graphic Novel', 'Hope Larson', 392, 500, 'Margaret Ferguson Bo', 'Graphic novel', 0),
(56, 'The Point of Light', 'John Ellsworth', 400, 100, 'N/A', 'Historical fiction', 0),
(57, 'India Gray: Historical Fiction Boxed Set', 'Sujata Massey', 100, 300, 'Paperback', 'Historical fiction', 0),
(58, 'Jaffa Beach: Historical Fiction', 'Fedora Horowitz', 454, 800, 'Createspace Independ', 'Historical fiction', 0),
(59, 'The Atlantis Plague', 'A.G. Riddle', 432, 800, 'Riddle Inc', 'Mystery', 1),
(60, 'Holy Island', 'L.J. Ross', 316, 500, 'Kindle Direct Publis', 'Mystery', 0),
(61, 'Mystery Man', 'Kristen Ashley', 464, 1000, 'N/A', 'Mystery', 1),
(62, 'A History of Western Philosophy', 'Bertrand Russell', 906, 1500, 'Simon & Schuster', 'Philosophy', 1),
(63, 'Discourse on Method and Meditations on First Philosophy', 'René Descartes, Donald A. Cress', 103, 300, 'Hackett Publishing C', 'Philosophy', 0),
(64, 'The Consolations of Philosophy', 'Alain de Botton', 265, 500, 'Vintage ', 'Philosophy', 0);

-- --------------------------------------------------------

--
-- Table structure for table `issue`
--

CREATE TABLE `issue` (
  `issue_id` int(11) NOT NULL,
  `book_id` int(11) DEFAULT NULL,
  `m_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `issue`
--

INSERT INTO `issue` (`issue_id`, `book_id`, `m_id`) VALUES
(3, 61, 5),
(4, 1, 4),
(6, 59, 1),
(7, 62, 7);

-- --------------------------------------------------------

--
-- Table structure for table `member`
--

CREATE TABLE `member` (
  `m_id` int(11) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `phone` int(11) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `status` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `member`
--

INSERT INTO `member` (`m_id`, `name`, `type`, `address`, `email`, `phone`, `gender`, `status`) VALUES
(1, 'nitesh asale', 'Student', 'akurdi', 'niteshasale358@gmail.com', 1234567890, 'Male', 1),
(2, 'santosh more', 'Lecturer', 'chinchwad ', 'santshmore@gmail.com', 1234567890, 'Male', 0),
(3, 'reshma', 'Lecturer', 'chinchwad', 'reshma@gmail.com', 1234567854, 'Female', 0),
(4, 'priyanka', 'Lecturer', 'pune', 'priyanka@gmail.com', 1234567890, 'Female', 1),
(5, 'neha ', 'Student', 'pune', 'neha@gmail.com', 123456790, 'Female', 1),
(6, 'john', 'Lecturer', 'chinchwad', 'john@gmail.com', 2147483647, 'Male', 0),
(7, 'sakshi', 'Student', 'pune', 'sakshi@gmail.com', 2147483647, 'Female', 1),
(8, 'pratik', 'Lecturer', 'chinchwad', 'bunty@gmail.com', 2147483647, 'Male', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`book_id`);

--
-- Indexes for table `issue`
--
ALTER TABLE `issue`
  ADD PRIMARY KEY (`issue_id`);

--
-- Indexes for table `member`
--
ALTER TABLE `member`
  ADD PRIMARY KEY (`m_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `book`
--
ALTER TABLE `book`
  MODIFY `book_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=65;

--
-- AUTO_INCREMENT for table `issue`
--
ALTER TABLE `issue`
  MODIFY `issue_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `member`
--
ALTER TABLE `member`
  MODIFY `m_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
