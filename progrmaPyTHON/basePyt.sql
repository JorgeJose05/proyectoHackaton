-- phpMyAdmin SQL Dump
-- version 6.0.0-dev
-- https://www.phpmyadmin.net/
--
-- Servidor: 192.168.30.22
-- Tiempo de generación: 05-04-2024 a las 15:12:47
-- Versión del servidor: 10.4.8-MariaDB-1:10.4.8+maria~stretch-log
-- Versión de PHP: 8.2.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `basePyt`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `DatosColumn`
--

CREATE TABLE `DatosColumn` (
  `sensor_id` int(11) NOT NULL,
  `dia` int(11) DEFAULT NULL,
  `hora` int(11) DEFAULT NULL,
  `minuto` int(11) DEFAULT NULL,
  `segundo` int(11) DEFAULT NULL,
  `medialluvia` double DEFAULT NULL,
  `nitrogenFinal` double DEFAULT NULL,
  `phosphorousFinal` double DEFAULT NULL,
  `potassiumFinal` double DEFAULT NULL,
  `radiacionSolar` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `DatosColumn`
--

INSERT INTO `DatosColumn` (`sensor_id`, `dia`, `hora`, `minuto`, `segundo`, `medialluvia`, `nitrogenFinal`, `phosphorousFinal`, `potassiumFinal`, `radiacionSolar`) VALUES
(1, 5, 12, 30, 45, 15.5, 25.3, 10.8, 5.7, 1200.5),
(2, 5, 12, 30, 46, 12.2, 24.5, 11.3, 6.1, 1150.2),
(3, 5, 12, 30, 47, 14.8, 23.9, 12.1, 5.5, 1185.7);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `DatosColumn`
--
ALTER TABLE `DatosColumn`
  ADD PRIMARY KEY (`sensor_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
