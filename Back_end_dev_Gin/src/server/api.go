package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"github.com/go-redis/redis"
	"net/http"
)

func init() {
	api := Router.Group("/api")
	{
		api.GET("/videos/", getVideos)
		api.GET("/videos/:designation/details/", getVideoDetails)
		api.PUT("/videos/:designation/", putVideo)
	}
}

func getVideos(c *gin.Context) {
	conn := RDB.Conn()
	defer conn.Close()

	keys, err := conn.Keys("l_*").Result()
	HandlerError(err)

	pipe := RDB.Pipeline()
	defer pipe.Close()

	for _, key := range keys {
		pipe.HGetAll(key)
	}
	result, err := pipe.Exec()

	var videos []map[string]string
	for _, videoI := range result {
		videoH := videoI.(*redis.StringStringMapCmd)
		videoMap := videoH.Val()
		videos = append(videos, videoMap)
	}

	c.JSON(http.StatusOK, videos)
}

func getVideoDetails(c *gin.Context) {
	designation, ok := c.Params.Get("designation")
	if !ok {
		c.AbortWithStatusJSON(http.StatusBadRequest, gin.H{
			"msg": "参数有误",
		})
	}

	conn := RDB.Conn()
	defer conn.Close()

	key := fmt.Sprintf("d_%s", designation)
	result, err := conn.Get(key).Result()
	HandlerError(err)

	c.Writer.Header()["Content-Type"] = []string{"application/json; charset=utf-8"}
	c.String(http.StatusOK, result)

}

type Video struct {
	IsLike string `json:"il"`
}

func putVideo(c *gin.Context) {
	designation, ok := c.Params.Get("designation")
	if !ok {
		c.AbortWithStatusJSON(http.StatusBadRequest, gin.H{
			"msg": "参数有误",
		})
	}

	var video Video
	err := c.BindJSON(&video)
	HandlerError(err)
	if err != nil {
		c.AbortWithStatusJSON(http.StatusBadRequest, gin.H{
			"msg": "参数有误",
		})
	}

	conn := RDB.Conn()
	defer conn.Close()

	key := fmt.Sprintf("l_%s", designation)
	err = conn.HSet(key, "il", video.IsLike).Err()
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{
			"result": err.Error(),
		})
	} else {
		c.JSON(http.StatusOK, gin.H{
			"result": "succeed",
		})
	}
}