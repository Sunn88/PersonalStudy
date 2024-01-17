package com.mysite.sbbPrj.user;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;

//3-6-2 회원 리포지터리 생성~
public interface UserRepository extends JpaRepository<SiteUser, Long> {
	//3-7-4 회원 리포지터리 수정~
	Optional<SiteUser> findByusername(String username);
	//~3-7-4 회원 리포지터리 수정
}
//~3-6-2 회원 리포지터리 생성