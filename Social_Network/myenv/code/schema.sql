drop table if exists posts;

create table posts(
    id int primary key,
    name text not null,
    content varchar not null
);