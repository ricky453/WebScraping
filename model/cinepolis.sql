-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 25-03-2021 a las 03:17:47
-- Versión del servidor: 10.4.17-MariaDB
-- Versión de PHP: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `cinepolis`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `funciones`
--

CREATE TABLE `funciones` (
  `idFuncion` int(11) NOT NULL,
  `idPelicula` varchar(150) NOT NULL,
  `pelicula` varchar(300) NOT NULL,
  `cine` varchar(300) NOT NULL,
  `departamento` varchar(100) NOT NULL,
  `tipo_doblaje` varchar(100) NOT NULL,
  `sala` varchar(100) NOT NULL,
  `asientosOcupados` int(11) DEFAULT NULL,
  `asientosTotales` int(11) DEFAULT NULL,
  `fechaFuncion` date NOT NULL,
  `horaFuncion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `funciones`
--

INSERT INTO `funciones` (`idFuncion`, `idPelicula`, `pelicula`, `cine`, `departamento`, `tipo_doblaje`, `sala`, `asientosOcupados`, `asientosTotales`, `fechaFuncion`, `horaFuncion`) VALUES
(1, 'get_ticket123', 'ATAQUE A LOS TITANES', 'CINEPOLIS GALERIAS', 'SAN SALVADOR', '', '1', NULL, NULL, '2021-03-22', '17:05'),
(2, 'get_ticket4321', 'CABALLEROS DEL ZODIACO', 'CINEPLIS METROCENTRO', 'SANTA ANA', '', '2', NULL, NULL, '2021-03-22', ''),
(3, 'get_ticket145', 'EL PEPE', 'CINEPOLIS SANTA ANA', 'SANTA ANA', 'TRADICIONAL', '2', NULL, NULL, '2021-03-24', '19:45');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `funciones`
--
ALTER TABLE `funciones`
  ADD PRIMARY KEY (`idFuncion`,`idPelicula`,`pelicula`,`departamento`,`sala`,`fechaFuncion`,`horaFuncion`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
