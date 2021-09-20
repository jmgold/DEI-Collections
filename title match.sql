SELECT
substr(title,1,3)||substr(title,instr(title,' ')+1,2)||,
Title

FROM
holdings

limit 50