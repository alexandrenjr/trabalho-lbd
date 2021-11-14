DROP TABLE IF EXISTS consulta_log;

CREATE TABLE consulta_log(
	old_cod_consulta INTEGER,
	new_cod_consulta INTEGER,
	old_data DATE,
	new_data DATE,
	old_hora TIME,
	new_hora TIME,
	old_local VARCHAR(50),
	new_local VARCHAR(50),
	old_especialidade VARCHAR(50),
	new_especialidade VARCHAR(50),
	cns_paciente VARCHAR(15),
	tipo_alteracao VARCHAR(6),
	data_alteracao TIMESTAMP WITH TIME ZONE
);

CREATE OR REPLACE FUNCTION consultalog() RETURNS TRIGGER AS $$
BEGIN
	IF TG_OP = 'UPDATE' THEN
	INSERT INTO consulta_log VALUES (old.cod_consulta, new.cod_consulta, old.data, new.data, 
									 old.hora, new.hora, old.local, new.local, old.especialidade,
									 new.especialidade, old.cns_paciente, 'UPDATE', NOW());
	ELSE
	INSERT INTO consulta_log VALUES (old.cod_consulta, new.cod_consulta, old.data, new.data, 
									 old.hora, new.hora, old.local, new.local, old.cns_paciente,
									 old.especialidade, new.especialidade 'DELETE', NOW());
	END IF;
	RETURN new;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER altera_consulta 
AFTER DELETE OR UPDATE ON consulta
FOR EACH ROW EXECUTE FUNCTION consultalog();