<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
  PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
  "http://mybatis.org/dtd/mybatis-3-mapper.dtd">

<mapper namespace="popteam.cinepic.dao.Mapper">

	<select id="selectAverage" parameterType="Review" resultType="double">
      select avg(score)
      from cinepic_review
      where mno = #{mno}
    </select>

	<select id="selectId" parameterType="User" resultType="User">
		select *
		from cinepic_user
		where id = #{id}
	</select>
	
	<insert id="insertUser" parameterType="User">
		insert into cinepic_user values (
		#{id}, #{pw}, #{name}, #{email}, #{phone}
		)
	</insert>
	
	<select id="selectUser" parameterType="User" resultType="User">
		select *
		from cinepic_user
		where id = #{id}
		and pw = #{pw}
	</select>
	
	<select id="findId" parameterType="User" resultType="User">
		select *
		from cinepic_user
		where name = #{name}
		and email = #{email}
		and phone = #{phone}
	</select>
	
	<select id="findPw" parameterType="User" resultType="User">
		select *
		from cinepic_user
		where id = #{id}
		and name = #{name}
		and email = #{email}
		and phone = #{phone}
	</select>
	
	<update id="updateUser" parameterType="User">
		update cinepic_user
		set pw = #{pw},
		email = #{email},
		phone = #{phone}
		where id = #{id}
	</update>
	
	<delete id="deleteUser" parameterType="User">
		delete cinepic_user
		where id = #{id}
		and pw = #{pw}
	</delete>
	
	<select id="selectAllMovie" parameterType="Movie" resultType="Movie">
		select *
		from cinepic_movie
		where title like '%'||#{title}||'%'
		or director like '%'||#{director}||'%'
		or actor like '%'||#{actor}||'%'	
	</select>
	
	<select id="selectMovie" parameterType="Movie" resultType="Movie">
		select *
		from cinepic_movie
		where mno = #{mno}	
	</select>
	
	<select id="selectAllReview" parameterType="Review" resultType="Review">
		select *
		from cinepic_review
		where mno = #{mno}
	</select>
	
	<insert id="insertReview" parameterType="Review">
		insert into cinepic_review values (
		#{mno}, #{id}, #{score}, #{review}
		)
	</insert>
	
	<delete id="deleteReview" parameterType="Review">
		delete cinepic_review
		where mno = #{mno} 
		and id = #{id}
	</delete>
	
	<select id="selectMyReview" parameterType="Review" resultType="Review">
		select *
		from cinepic_review
		where id = #{id}
	</select>
</mapper>
