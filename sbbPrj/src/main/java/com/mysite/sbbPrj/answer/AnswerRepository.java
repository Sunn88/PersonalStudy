package com.mysite.sbbPrj.answer;

import org.springframework.data.jpa.repository.JpaRepository;

//2-5-2 답변 리포지토리 생성~
public interface AnswerRepository extends JpaRepository<Answer, Integer> {
	//~2-5-2 답변 리포지토리 생성
}