create table user(
    id text primary key,
    name text not null,
    email unique no null,
    profile_pic not null
);