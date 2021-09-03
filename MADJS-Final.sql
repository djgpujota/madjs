-- Database generated with pgModeler (PostgreSQL Database Modeler).
-- pgModeler  version: 0.7.2
-- PostgreSQL version: 9.4
-- Project Site: pgmodeler.com.br
-- Model Author: ---

SET check_function_bodies = false;
-- ddl-end --


-- Database creation must be done outside an multicommand file.
-- These commands were put in this file only for convenience.
-- -- object: new_database | type: DATABASE --
-- -- DROP DATABASE new_database;
-- CREATE DATABASE new_database
-- ;
-- -- ddl-end --
-- 

-- object: public.personas | type: TABLE --
-- DROP TABLE public.personas;
CREATE TABLE public.personas(
	id_personas integer NOT NULL,
	id_rol integer NOT NULL,
	nombre_personas character varying(75) NOT NULL,
	dir_personas character varying(75) NOT NULL,
	telf_personas integer NOT NULL,
	email_personas character varying(30) NOT NULL,
	clave_personas character varying(25) NOT NULL,
	estado integer NOT NULL,
	CONSTRAINT id_personas PRIMARY KEY (id_personas)

);
-- ddl-end --
-- object: public.rol | type: TABLE --
-- DROP TABLE public.rol;
CREATE TABLE public.rol(
	id_rol integer NOT NULL,
	usuario_rol character varying(15) NOT NULL,
	permisos_rol integer NOT NULL,
	CONSTRAINT id_rol PRIMARY KEY (id_rol)

);
-- ddl-end --
-- object: public.proveedor | type: TABLE --
-- DROP TABLE public.proveedor;
CREATE TABLE public.proveedor(
	id_proveedor integer NOT NULL,
	nombre_proveedor character varying(75) NOT NULL,
	ruc_proveedor varchar(13) NOT NULL,
	dir_proveedor character varying(75),
	telf_proveedor integer NOT NULL,
	email_proveedor character(30) NOT NULL,
	CONSTRAINT id_proveedor PRIMARY KEY (id_proveedor)

);
-- ddl-end --
-- object: public.producto_ingresado | type: TABLE --
-- DROP TABLE public.producto_ingresado;
CREATE TABLE public.producto_ingresado(
	id_producto_ingresado integer NOT NULL,
	id_proveedor integer NOT NULL,
	nombre_producto_ingresado character varying(50) NOT NULL,
	precio_producto_ingresado numeric(12,1) NOT NULL,
	cantidad_producto_ingresado integer NOT NULL,
	imagen_producto_ingresado varchar(5000) NOT NULL,
	categoria_productos character varying(55) NOT NULL,
	CONSTRAINT id_producto_ingresado PRIMARY KEY (id_producto_ingresado)

);
-- ddl-end --
-- object: public.producto_salida | type: TABLE --
-- DROP TABLE public.producto_salida;
CREATE TABLE public.producto_salida(
	id_producto_salida integer NOT NULL,
	id_aceptar_reserva integer NOT NULL,
	nombre_producto_salida character varying(50) NOT NULL,
	precio_producto_salida decimal(12,2) NOT NULL,
	cantidad_vendida_producto_salida integer NOT NULL,
	CONSTRAINT "id_producto_empresa.mad.js" PRIMARY KEY (id_producto_salida)

);
-- ddl-end --
-- object: public.ordenes_clientes | type: TABLE --
-- DROP TABLE public.ordenes_clientes;
CREATE TABLE public.ordenes_clientes(
	id_ordenes_clientes integer NOT NULL,
	id_personas integer NOT NULL,
	id_producto_ingresado integer NOT NULL,
	subtotal_ordenes_clientes decimal(12,2) NOT NULL,
	nombre_ordenes_cliente varchar(55) NOT NULL,
	cantidad_ordenes_cliente integer NOT NULL,
	cedula_ordenes_cliente integer NOT NULL,
	correo_ordenes_clientes varchar(55) NOT NULL,
	categoria_ordenes_cliente varchar(55) NOT NULL,
	fecha_ordenes_cliente date NOT NULL,
	estado integer NOT NULL,
	CONSTRAINT id_ordenes_clientes PRIMARY KEY (id_ordenes_clientes)

);
-- ddl-end --
-- object: public.aceptar_reserva | type: TABLE --
-- DROP TABLE public.aceptar_reserva;
CREATE TABLE public.aceptar_reserva(
	id_aceptar_reserva integer NOT NULL,
	id_ordenes_clientes integer NOT NULL,
	estado_aceptar_reserva integer NOT NULL,
	CONSTRAINT id_aceptar_reserva PRIMARY KEY (id_aceptar_reserva)

);
-- ddl-end --
-- object: id_rol | type: CONSTRAINT --
-- ALTER TABLE public.personas DROP CONSTRAINT id_rol;
ALTER TABLE public.personas ADD CONSTRAINT id_rol FOREIGN KEY (id_rol)
REFERENCES public.rol (id_rol) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --


-- object: id_proveedor | type: CONSTRAINT --
-- ALTER TABLE public.producto_ingresado DROP CONSTRAINT id_proveedor;
ALTER TABLE public.producto_ingresado ADD CONSTRAINT id_proveedor FOREIGN KEY (id_proveedor)
REFERENCES public.proveedor (id_proveedor) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --


-- object: id_aceptar_reserva | type: CONSTRAINT --
-- ALTER TABLE public.producto_salida DROP CONSTRAINT id_aceptar_reserva;
ALTER TABLE public.producto_salida ADD CONSTRAINT id_aceptar_reserva FOREIGN KEY (id_aceptar_reserva)
REFERENCES public.aceptar_reserva (id_aceptar_reserva) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --


-- object: id_personas | type: CONSTRAINT --
-- ALTER TABLE public.ordenes_clientes DROP CONSTRAINT id_personas;
ALTER TABLE public.ordenes_clientes ADD CONSTRAINT id_personas FOREIGN KEY (id_personas)
REFERENCES public.personas (id_personas) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --


-- object: id_producto_ingresado | type: CONSTRAINT --
-- ALTER TABLE public.ordenes_clientes DROP CONSTRAINT id_producto_ingresado;
ALTER TABLE public.ordenes_clientes ADD CONSTRAINT id_producto_ingresado FOREIGN KEY (id_producto_ingresado)
REFERENCES public.producto_ingresado (id_producto_ingresado) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --


-- object: id_ordenes_clientes | type: CONSTRAINT --
-- ALTER TABLE public.aceptar_reserva DROP CONSTRAINT id_ordenes_clientes;
ALTER TABLE public.aceptar_reserva ADD CONSTRAINT id_ordenes_clientes FOREIGN KEY (id_ordenes_clientes)
REFERENCES public.ordenes_clientes (id_ordenes_clientes) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --



