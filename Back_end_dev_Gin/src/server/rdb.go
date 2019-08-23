package main

import "github.com/go-redis/redis"

var RDB = redis.NewClient(&redis.Options{
	Addr:     "192.168.217.132:6379",
	Password: "",
	DB:       0,
})
