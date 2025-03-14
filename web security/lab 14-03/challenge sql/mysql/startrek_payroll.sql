SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


--
-- Database: `payroll0`
--

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `username` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `salary` int(20) NOT NULL,
  `flag`  varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`username`, `first_name`, `last_name`, `password`, `salary`, `flag`) VALUES
('user','user','user','user','0','flag{not_the_flag}'),
('james_kirk','James','Kirk','kobayashi_maru','25000', 'flag{not_the_flag}'),
('mr_spock','Mr','Spock','0nlyL0g!c','99000','flag{not_the_flag}'),
('leonard_mccoy','Leonard','McCoy','hesDEADjim!','45000','flag{not_the_flag}'),
('nyota_uhura','Nyota','Uhura','StarShine','39000','flag{not_the_flag}'),
('montgomery_scott','Montgomery','Scott','ScottyDoesntKnow','1250','flag{not_the_flag}'),
('hiraku_sulu','Hikaru','Sulu','parking-break-on','3500','flag{not_the_flag}'),
('pavel_chekov','Pavel','Chekov','99victorvictor2','2500','flag{not_the_flag}'),
('random','random','ramdom','random','9999','flag{real_flag}');

