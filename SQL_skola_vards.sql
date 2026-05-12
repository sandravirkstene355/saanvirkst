insert or ignore into audzekni values("A_103","Kate","Svarinska","10b",16,01.09,53.40);
insert or ignore into audzekni values("A_104","Elīna","Pļava","11a",17,01.09,80.87);
select Audzekna_id, Vards, Uzvards, Klase, Vecums, iestasanas_datums, Stipendija from audzekni;
select sum(Stipendija) from audzekni;
select max(Stipendija) from audzekni;
select avg(Vecums) from audzekni;
select min(Vecums) from audzekni;
select Vards,Uzvards,Stipendija from audzekni;