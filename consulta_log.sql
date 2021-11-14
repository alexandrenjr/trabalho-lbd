
create table consulta_log(
	old_cod_consulta integer,
	new_cod_consulta integer,
	old_data date,
	new_data date,
	old_hora time,
	new_hora time,
	old_local varchar(50),
	new_local varchar(50),
	cns_paciente varchar(15),
	tipo_alteracao varchar(6),
	data_alteracao timestamp with time zone
);

create or replace function consultalog() returns trigger as $$
begin
	IF TG_OP = 'UPDATE' THEN
	insert into consulta_log values (old.cod_consulta, new.cod_consulta, old.data, new.data, 
									 old.hora, new.hora, old.local, new.local, old.cns_paciente, 
									 'UPDATE', now());
	ELSE
	insert into consulta_log values (old.cod_consulta, new.cod_consulta, old.data, new.data, 
									 old.hora, new.hora, old.local, new.local, old.cns_paciente, 
									 'DELETE', now());
	END IF;
	return new;
end;
$$ language plpgsql;

create trigger altera_consulta 
after delete or update of local on consulta
for each row execute function consultalog();