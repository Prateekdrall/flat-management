

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";



--
-- Database: `flat`
--

-- --------------------------------------------------------

--
-- Table structure for table `bill`
--

CREATE TABLE `bill` (
  `bill_id` bigint(20) NOT NULL,
   `book_id` bigint(20) DEFAULT NULL,
  `amount` float(10,2) DEFAULT NULL,
  `bill_date` date DEFAULT NULL,
  `water_electric_expens` int(10) DEFAULT NULL,
  `maintenance` int(10) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bill`
--

INSERT INTO `bill` (`bill_id`, `book_id`, `amount`, `bill_date`, `water_electric_expens`, `maintenance`) VALUES
(1, 1, 770500.00, '2020-12-25', 0, 0),
(2, 2, 500.00, '2020-12-25', 0, 0),
(3, 3, 1600.00, '2020-12-25', 0, 0),
(4, 4, 63000.00, '2020-12-25', 0, 0),
(5, 5, 10500.00, '2020-12-25', 0, 0),
(6, 6, 8000.00, '2020-12-25', 0, 0),
(7, 7, 10500.00, '2020-12-25', 23, 5),
(8, 8, 11500.00, '2020-12-25', 23, 5),
(9, 10, -3400.00, '2020-12-29', 23, 5),
(10, 15, 1866000.00, '2022-11-17', 0, 0),
(11, 16, 1250000.00, '2022-11-17', 0, 0),
(12, 18, 2876000.00, '2022-11-17', 0, 0),
(13, 19, 2876000.00, '2022-11-17', 0, 0),
(14, 20, 172000.00, '2022-11-20', 1000, 1000);

-- --------------------------------------------------------

--
-- Table structure for table `booking_details`
--

CREATE TABLE `booking_details` (
  `book_id` bigint(20) NOT NULL,
  `flat_id` bigint(20) DEFAULT NULL,
  `cust_id` bigint(20) DEFAULT NULL,
  `doo` date DEFAULT NULL,
  `dol` date DEFAULT NULL,
  `advance` float(10,2) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `booking_details`
--

INSERT INTO `booking_details` (`book_id`, `flat_id`, `cust_id`, `doo`, `dol`, `advance`) VALUES
(20, 411, 10, '2022-05-11', '2022-11-20', 10000.00);

-- --------------------------------------------------------

--
-- Table structure for table `customer_details`
--

CREATE TABLE `customer_details` (
  `id` bigint(20) NOT NULL,
  `name` char(50) DEFAULT NULL,
  `address` char(100) DEFAULT NULL,
  `phone` char(15) DEFAULT NULL,
  `email` char(80) DEFAULT NULL,
  `males` int(2) DEFAULT NULL,
  `females` int(2) DEFAULT NULL,
  `children` int(2) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customer_details`
--

INSERT INTO `customer_details` (`id`, `name`, `address`, `phone`, `email`, `males`, `females`, `children`) VALUES
(1, 'rakesh kumar', 'CF-4 BRIJ VIHAR', '98718168101', 'RAKESH@GMAIL.COM', 1, 1, 2),
(2, 'ajmal khan', 'F-234 BRIJ VIHAR', '456465456', 'AJMAL@GMAIL.COM', 2, 0, 0),
(4, 'naman', 'C-7 PITAMPURA', '7428196996', 'NAMAN@GMAIL.COM', 2, 2, 0),
(5, 'utkarsh', 'DWARKA MOR', '954432563', 'UTKARSH@GMAIL.COM', 3, 2, 1),
(6, 'sharil', 'UTTAM NAGAR', '96436453', 'SHARILMALIK@GMAIL.COM', 2, 1, 1),
(7, 'sanjeev', 'TILAK NAGAR', '9868610081', 'SANJU@GMAIL.COM', 3, 2, 2),
(8, 'utk', 'UTTAM NAGAR', '53423423', 'UTK@GMAIL.COM', 4, 0, 0),
(9, 'shreya', 'PUNJABI BAGH', '9968044775', 'SHREYA@GMAIL.COM', 2, 2, 0),
(10, 'lakshya', 'SRE', '7351820307', 'abc.gmail.com', 1, 0, 12);

-- --------------------------------------------------------

--
-- Table structure for table `flat`
--

CREATE TABLE `flat` (
  `flat_no` int(4) NOT NULL,
  `flat_type` char(20) DEFAULT NULL,
  `flat_rent` float(10,2) DEFAULT NULL,
  `flat_bed` char(20) DEFAULT NULL,
  `status` char(20) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `flat`
--

INSERT INTO `flat` (`flat_no`, `flat_type`, `flat_rent`, `flat_bed`, `status`) VALUES
(500, 'AC', 2650.00, 'SINGLE', 'free'),
(1, 'AC', 13000.00, 'DOUBLE', 'free'),
(250, ' AC', 3500.00, 'SINGLE', 'free'),
(1234, 'AC', 10000.00, 'TRIPLE', 'free'),
(411, 'AC', 30000.00, 'SINGLE', 'free');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bill`
--
ALTER TABLE `bill`
  ADD PRIMARY KEY (`bill_id`);

--
-- Indexes for table `booking_details`
--
ALTER TABLE `booking_details`
  ADD PRIMARY KEY (`book_id`);

--
-- Indexes for table `customer_details`
--
ALTER TABLE `customer_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `flat`
--
ALTER TABLE `flat`
  ADD PRIMARY KEY (`flat_no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bill`
--
ALTER TABLE `bill`
  MODIFY `bill_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `booking_details`
--
ALTER TABLE `booking_details`
  MODIFY `book_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `customer_details`
--
ALTER TABLE `customer_details`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;
