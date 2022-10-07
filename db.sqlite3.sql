BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_migrations" (
	"id"	integer NOT NULL,
	"app"	varchar(255) NOT NULL,
	"name"	varchar(255) NOT NULL,
	"applied"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
	"id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_user_groups" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "django_admin_log" (
	"id"	integer NOT NULL,
	"action_time"	datetime NOT NULL,
	"object_id"	text,
	"object_repr"	varchar(200) NOT NULL,
	"change_message"	text NOT NULL,
	"content_type_id"	integer,
	"user_id"	integer NOT NULL,
	"action_flag"	smallint unsigned NOT NULL CHECK("action_flag" >= 0),
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "app1_catalogo_perfiles" (
	"id"	integer NOT NULL,
	"Perfil"	varchar(30) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "app1_instructores" (
	"id"	integer NOT NULL,
	"NumeroDocumento"	varchar(20) NOT NULL,
	"TipoDocumento"	varchar(2) NOT NULL,
	"Nombre"	varchar(50) NOT NULL,
	"Apellido"	varchar(50) NOT NULL,
	"correoElectronico"	varchar(254) NOT NULL,
	"numeroCelular"	varchar(10) NOT NULL,
	"id_Perfiles_id"	bigint,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("id_Perfiles_id") REFERENCES "app1_catalogo_perfiles"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "django_content_type" (
	"id"	integer NOT NULL,
	"app_label"	varchar(100) NOT NULL,
	"model"	varchar(100) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_permission" (
	"id"	integer NOT NULL,
	"content_type_id"	integer NOT NULL,
	"codename"	varchar(100) NOT NULL,
	"name"	varchar(255) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_group" (
	"id"	integer NOT NULL,
	"name"	varchar(150) NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_user" (
	"id"	integer NOT NULL,
	"password"	varchar(128) NOT NULL,
	"last_login"	datetime,
	"is_superuser"	bool NOT NULL,
	"username"	varchar(150) NOT NULL UNIQUE,
	"last_name"	varchar(150) NOT NULL,
	"email"	varchar(254) NOT NULL,
	"is_staff"	bool NOT NULL,
	"is_active"	bool NOT NULL,
	"date_joined"	datetime NOT NULL,
	"first_name"	varchar(150) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_session" (
	"session_key"	varchar(40) NOT NULL,
	"session_data"	text NOT NULL,
	"expire_date"	datetime NOT NULL,
	PRIMARY KEY("session_key")
);
CREATE TABLE IF NOT EXISTS "app1_contratacion" (
	"id"	integer NOT NULL,
	"Fecha_Inicio"	date NOT NULL,
	"Fecha_Fin"	date NOT NULL,
	"horasMensualFormacion"	integer,
	"id_Instructor_id"	bigint,
	"supervisora"	varchar(50),
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("id_Instructor_id") REFERENCES "app1_instructores"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "app1_fichascaracterizacion" (
	"id"	integer NOT NULL,
	"ficha"	varchar(10) NOT NULL,
	"FechaInicioEtapaLectiva"	date NOT NULL,
	"FechaFinEtapaLectiva"	date NOT NULL,
	"Jornada"	varchar(10) NOT NULL,
	"CantidadAprendices"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "django_migrations" VALUES (1,'contenttypes','0001_initial','2022-04-19 11:59:35.452679');
INSERT INTO "django_migrations" VALUES (2,'auth','0001_initial','2022-04-19 11:59:35.559612');
INSERT INTO "django_migrations" VALUES (3,'admin','0001_initial','2022-04-19 11:59:35.639285');
INSERT INTO "django_migrations" VALUES (4,'admin','0002_logentry_remove_auto_add','2022-04-19 11:59:35.728599');
INSERT INTO "django_migrations" VALUES (5,'admin','0003_logentry_add_action_flag_choices','2022-04-19 11:59:35.788285');
INSERT INTO "django_migrations" VALUES (6,'app1','0001_initial','2022-04-19 11:59:35.879801');
INSERT INTO "django_migrations" VALUES (7,'contenttypes','0002_remove_content_type_name','2022-04-19 11:59:35.934397');
INSERT INTO "django_migrations" VALUES (8,'auth','0002_alter_permission_name_max_length','2022-04-19 11:59:35.982432');
INSERT INTO "django_migrations" VALUES (9,'auth','0003_alter_user_email_max_length','2022-04-19 11:59:36.044398');
INSERT INTO "django_migrations" VALUES (10,'auth','0004_alter_user_username_opts','2022-04-19 11:59:36.080048');
INSERT INTO "django_migrations" VALUES (11,'auth','0005_alter_user_last_login_null','2022-04-19 11:59:36.129406');
INSERT INTO "django_migrations" VALUES (12,'auth','0006_require_contenttypes_0002','2022-04-19 11:59:36.168220');
INSERT INTO "django_migrations" VALUES (13,'auth','0007_alter_validators_add_error_messages','2022-04-19 11:59:36.207769');
INSERT INTO "django_migrations" VALUES (14,'auth','0008_alter_user_username_max_length','2022-04-19 11:59:36.258591');
INSERT INTO "django_migrations" VALUES (15,'auth','0009_alter_user_last_name_max_length','2022-04-19 11:59:36.304447');
INSERT INTO "django_migrations" VALUES (16,'auth','0010_alter_group_name_max_length','2022-04-19 11:59:36.346618');
INSERT INTO "django_migrations" VALUES (17,'auth','0011_update_proxy_permissions','2022-04-19 11:59:36.391709');
INSERT INTO "django_migrations" VALUES (18,'auth','0012_alter_user_first_name_max_length','2022-04-19 11:59:36.442272');
INSERT INTO "django_migrations" VALUES (19,'sessions','0001_initial','2022-04-19 11:59:36.509353');
INSERT INTO "django_migrations" VALUES (20,'app1','0002_contratacion_supervisora','2022-04-19 12:27:04.469620');
INSERT INTO "django_migrations" VALUES (21,'app1','0003_fichascaracterizacion','2022-08-20 14:35:05.755638');
INSERT INTO "auth_user_user_permissions" VALUES (1,2,40);
INSERT INTO "auth_user_user_permissions" VALUES (2,2,1);
INSERT INTO "auth_user_user_permissions" VALUES (3,2,29);
INSERT INTO "auth_user_user_permissions" VALUES (4,3,1);
INSERT INTO "auth_user_user_permissions" VALUES (5,3,3);
INSERT INTO "auth_user_user_permissions" VALUES (6,3,4);
INSERT INTO "auth_user_user_permissions" VALUES (7,3,25);
INSERT INTO "auth_user_user_permissions" VALUES (8,3,26);
INSERT INTO "auth_user_user_permissions" VALUES (9,3,27);
INSERT INTO "auth_user_user_permissions" VALUES (10,3,28);
INSERT INTO "auth_user_user_permissions" VALUES (11,3,29);
INSERT INTO "auth_user_user_permissions" VALUES (12,3,30);
INSERT INTO "auth_user_user_permissions" VALUES (13,3,31);
INSERT INTO "auth_user_user_permissions" VALUES (14,3,32);
INSERT INTO "auth_user_user_permissions" VALUES (15,3,33);
INSERT INTO "auth_user_user_permissions" VALUES (16,3,34);
INSERT INTO "auth_user_user_permissions" VALUES (17,3,35);
INSERT INTO "auth_user_user_permissions" VALUES (18,3,36);
INSERT INTO "auth_user_user_permissions" VALUES (19,3,37);
INSERT INTO "auth_user_user_permissions" VALUES (20,3,38);
INSERT INTO "auth_user_user_permissions" VALUES (21,3,39);
INSERT INTO "auth_user_user_permissions" VALUES (22,3,40);
INSERT INTO "django_admin_log" VALUES (1,'2022-09-22 19:19:26.164225','2','apoyo','[{"added": {}}]',4,1,1);
INSERT INTO "django_admin_log" VALUES (2,'2022-09-22 19:22:38.963613','2','apoyo','[{"changed": {"fields": ["First name", "Last name", "Email address"]}}]',4,1,2);
INSERT INTO "django_admin_log" VALUES (3,'2022-09-22 19:24:16.589195','3','coordinador','[{"added": {}}]',4,1,1);
INSERT INTO "django_admin_log" VALUES (4,'2022-09-22 19:24:52.495510','3','coordinador','[{"changed": {"fields": ["First name", "Last name", "Email address"]}}]',4,1,2);
INSERT INTO "django_admin_log" VALUES (5,'2022-09-26 18:02:15.403547','2','apoyo','[{"changed": {"fields": ["User permissions"]}}]',4,1,2);
INSERT INTO "django_admin_log" VALUES (6,'2022-09-26 18:04:03.636956','3','coordinador','[{"changed": {"fields": ["User permissions"]}}]',4,1,2);
INSERT INTO "app1_instructores" VALUES (7,'1234567','CC','Nelson','Diaz','ngdiaz02@misena.edu.co','3162919901',NULL);
INSERT INTO "app1_instructores" VALUES (8,'7654321','CC','Darwin','Celis','darwin@sena.edu.co','325487455',NULL);
INSERT INTO "app1_instructores" VALUES (9,'1478523','CC','Oscar','Campos','campososcar@gmail.com','987255665',NULL);
INSERT INTO "app1_instructores" VALUES (10,'7412234','CE','Ivon','Forero','if5@outlook.com','3248299946',NULL);
INSERT INTO "app1_instructores" VALUES (11,'5547415','CE','Carlos','Gutierrez','cargut@gmail.com','259954566',NULL);
INSERT INTO "app1_instructores" VALUES (12,'6552114','CC','Gabriel','Hernandez','gabhernandez@outlook.com','364488996',NULL);
INSERT INTO "app1_instructores" VALUES (13,'15896666','CC','Javier','Diaz','javierdiaz02@misena.edu.co','3162919907',NULL);
INSERT INTO "app1_instructores" VALUES (14,'158977886','CC','Nelson','Diez','diezn@misena.edu.co','3162919907',NULL);
INSERT INTO "django_content_type" VALUES (1,'admin','logentry');
INSERT INTO "django_content_type" VALUES (2,'auth','permission');
INSERT INTO "django_content_type" VALUES (3,'auth','group');
INSERT INTO "django_content_type" VALUES (4,'auth','user');
INSERT INTO "django_content_type" VALUES (5,'contenttypes','contenttype');
INSERT INTO "django_content_type" VALUES (6,'sessions','session');
INSERT INTO "django_content_type" VALUES (7,'app1','catalogo_perfiles');
INSERT INTO "django_content_type" VALUES (8,'app1','instructores');
INSERT INTO "django_content_type" VALUES (9,'app1','contratacion');
INSERT INTO "django_content_type" VALUES (10,'app1','fichascaracterizacion');
INSERT INTO "auth_permission" VALUES (1,1,'add_logentry','Can add log entry');
INSERT INTO "auth_permission" VALUES (2,1,'change_logentry','Can change log entry');
INSERT INTO "auth_permission" VALUES (3,1,'delete_logentry','Can delete log entry');
INSERT INTO "auth_permission" VALUES (4,1,'view_logentry','Can view log entry');
INSERT INTO "auth_permission" VALUES (5,2,'add_permission','Can add permission');
INSERT INTO "auth_permission" VALUES (6,2,'change_permission','Can change permission');
INSERT INTO "auth_permission" VALUES (7,2,'delete_permission','Can delete permission');
INSERT INTO "auth_permission" VALUES (8,2,'view_permission','Can view permission');
INSERT INTO "auth_permission" VALUES (9,3,'add_group','Can add group');
INSERT INTO "auth_permission" VALUES (10,3,'change_group','Can change group');
INSERT INTO "auth_permission" VALUES (11,3,'delete_group','Can delete group');
INSERT INTO "auth_permission" VALUES (12,3,'view_group','Can view group');
INSERT INTO "auth_permission" VALUES (13,4,'add_user','Can add user');
INSERT INTO "auth_permission" VALUES (14,4,'change_user','Can change user');
INSERT INTO "auth_permission" VALUES (15,4,'delete_user','Can delete user');
INSERT INTO "auth_permission" VALUES (16,4,'view_user','Can view user');
INSERT INTO "auth_permission" VALUES (17,5,'add_contenttype','Can add content type');
INSERT INTO "auth_permission" VALUES (18,5,'change_contenttype','Can change content type');
INSERT INTO "auth_permission" VALUES (19,5,'delete_contenttype','Can delete content type');
INSERT INTO "auth_permission" VALUES (20,5,'view_contenttype','Can view content type');
INSERT INTO "auth_permission" VALUES (21,6,'add_session','Can add session');
INSERT INTO "auth_permission" VALUES (22,6,'change_session','Can change session');
INSERT INTO "auth_permission" VALUES (23,6,'delete_session','Can delete session');
INSERT INTO "auth_permission" VALUES (24,6,'view_session','Can view session');
INSERT INTO "auth_permission" VALUES (25,7,'add_catalogo_perfiles','Can add catalogo_ perfiles');
INSERT INTO "auth_permission" VALUES (26,7,'change_catalogo_perfiles','Can change catalogo_ perfiles');
INSERT INTO "auth_permission" VALUES (27,7,'delete_catalogo_perfiles','Can delete catalogo_ perfiles');
INSERT INTO "auth_permission" VALUES (28,7,'view_catalogo_perfiles','Can view catalogo_ perfiles');
INSERT INTO "auth_permission" VALUES (29,8,'add_instructores','Can add instructores');
INSERT INTO "auth_permission" VALUES (30,8,'change_instructores','Can change instructores');
INSERT INTO "auth_permission" VALUES (31,8,'delete_instructores','Can delete instructores');
INSERT INTO "auth_permission" VALUES (32,8,'view_instructores','Can view instructores');
INSERT INTO "auth_permission" VALUES (33,9,'add_contratacion','Can add contratacion');
INSERT INTO "auth_permission" VALUES (34,9,'change_contratacion','Can change contratacion');
INSERT INTO "auth_permission" VALUES (35,9,'delete_contratacion','Can delete contratacion');
INSERT INTO "auth_permission" VALUES (36,9,'view_contratacion','Can view contratacion');
INSERT INTO "auth_permission" VALUES (37,10,'add_fichascaracterizacion','Can add fichas caracterizacion');
INSERT INTO "auth_permission" VALUES (38,10,'change_fichascaracterizacion','Can change fichas caracterizacion');
INSERT INTO "auth_permission" VALUES (39,10,'delete_fichascaracterizacion','Can delete fichas caracterizacion');
INSERT INTO "auth_permission" VALUES (40,10,'view_fichascaracterizacion','Can view fichas caracterizacion');
INSERT INTO "auth_user" VALUES (1,'pbkdf2_sha256$320000$aKUsDHFjUI7q1uk6Luh9Tw$LLYRx0u8vR4wD78i2OVnrBpMG6GBG/OS6pT0E0Zr0ZQ=','2022-09-22 19:09:24.184113',1,'admin','','proyectop392@gmail.com',1,1,'2022-09-22 19:07:14.578992','');
INSERT INTO "auth_user" VALUES (2,'pbkdf2_sha256$320000$rbCjLfXGTVlZZk3ifbGqAv$KPjP5w1oNBDvjZ2bmWy/nrIe9eg0kOPOnE6+pSYYaso=',NULL,0,'apoyo','Sierra','casierra68@misena.edu.co',0,1,'2022-09-22 19:19:25','Carol');
INSERT INTO "auth_user" VALUES (3,'pbkdf2_sha256$320000$JHIRFnYJy3vdpUVeZXR5vV$X6CVD8sFtX5xDrtjvgiJw+/TXNDQvRJLRN6tsr50/8Y=',NULL,0,'coordinador','Juyo','sierracarol14@gmail.com',0,1,'2022-09-22 19:24:16','Fabian');
INSERT INTO "django_session" VALUES ('5gp5j9ogbj553lh11rsb6svlvaevwz36','.eJxVjEEOwiAQRe_C2pApA4W6dO8ZyACDVA0kpV0Z765NutDtf-_9l_C0rcVvnRc_J3EWgzj9boHig-sO0p3qrcnY6rrMQe6KPGiX15b4eTncv4NCvXxrA1phsiM5PaDJyoUEPNoJbKCEEzhiiiYzGIUIgNYSB8ykWbMNSon3B8e5N44:1obRZc:wirdmL9q-NGyGM_dIidwCLkuCzLXW4vc0ypUNjWVBM8','2022-10-06 19:09:24.329098');
INSERT INTO "app1_contratacion" VALUES (7,'2022-01-02','2022-01-11',160,7,'Sandra Liliana');
INSERT INTO "app1_contratacion" VALUES (8,'2022-01-02','2022-01-11',132,8,'Sandra Liliana');
INSERT INTO "app1_contratacion" VALUES (9,'2022-01-02','2022-01-11',132,9,'Daniel Perez');
INSERT INTO "app1_contratacion" VALUES (10,'2022-01-02','2022-01-11',160,10,'Daniel Perez');
INSERT INTO "app1_contratacion" VALUES (11,'2022-01-02','2022-01-11',160,11,'Yamile Espitia');
INSERT INTO "app1_contratacion" VALUES (12,'2022-01-02','2022-01-11',160,12,'Pedro Buitrago');
INSERT INTO "app1_contratacion" VALUES (13,'2022-01-02','2022-01-11',160,13,'Sandra Liliana');
INSERT INTO "app1_contratacion" VALUES (14,'2022-01-02','2022-01-11',160,14,'Sandra Liliana');
CREATE UNIQUE INDEX IF NOT EXISTS "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" (
	"group_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" (
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" (
	"permission_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" (
	"user_id",
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_group_id_97559544" ON "auth_user_groups" (
	"group_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" (
	"user_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_user_id_c564eba6" ON "django_admin_log" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "app1_instructores_id_Perfiles_id_3cfb600a" ON "app1_instructores" (
	"id_Perfiles_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" (
	"app_label",
	"model"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" (
	"content_type_id",
	"codename"
);
CREATE INDEX IF NOT EXISTS "auth_permission_content_type_id_2f476e4b" ON "auth_permission" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_session_expire_date_a5c62663" ON "django_session" (
	"expire_date"
);
CREATE INDEX IF NOT EXISTS "app1_contratacion_id_Instructor_id_be10a234" ON "app1_contratacion" (
	"id_Instructor_id"
);
COMMIT;
