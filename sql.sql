create table cinepic_user (
id varchar2(30) primary key,
pw varchar2(60) not null,
name varchar2(30) not null,
email varchar2(90) not null,
phone varchar2(60) not null 
);

create table cinepic_movie (
mno number primary key,
title varchar2(300) not null,
genre varchar2(300) not null,
director varchar2(300) not null,
actor varchar2(300) not null,
poster varchar2(300) not null
);

create table cinepic_review (
mno number references cinepic_movie(mno),
id varchar2(30) references cinepic_user(id),
score number not null,
review varchar2(300)
);

drop table cinepic_user;
drop table cinepic_movie;
drop table cinepic_review;
