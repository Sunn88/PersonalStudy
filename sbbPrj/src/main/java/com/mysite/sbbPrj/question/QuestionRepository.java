package com.mysite.sbbPrj.question;

import java.util.List;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.domain.Specification;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

//2-5-1 질문 리포지토리 생성~
public interface QuestionRepository extends JpaRepository<Question, Integer> {
	//~2-5-1 질문 리포지토리 생성
	//2-5-7-1 findBySubject 메소드~
	Question findBySubject(String subject);
	//~2-5-7-1 findBySubject 메소드
	//2-5-9-1 findBySubjectAndContent 메소드~
	Question findBySubjectAndContent(String subject, String content);
	//~2-5-9-1 findBySubjectAndContent 메소드
	//2-5-10-1 findBySubjectLike 메소드~
	List<Question> findBySubjectLike(String subject);
	//~2-5-10-1 findBySubjectLike 메소드
	//3-2-1 질문 페이징~
    Page<Question> findAll(Pageable pageable);
	//~3-2-1 질문 페이징
    //3-13-2 질문 검색~
    Page<Question> findAll(Specification<Question> spec, Pageable pageable);
    //~3-13-2 질문 검색
    //3-13-9-1 쿼리 검색 기능~
    @Query("select "
            + "distinct q "
            + "from Question q " 
            + "left outer join SiteUser u1 on q.author=u1 "
            + "left outer join Answer a on a.question=q "
            + "left outer join SiteUser u2 on a.author=u2 "
            + "where "
            + "   q.subject like %:kw% "
            + "   or q.content like %:kw% "
            + "   or u1.username like %:kw% "
            + "   or a.content like %:kw% "
            + "   or u2.username like %:kw% ")
    Page<Question> findAllByKeyword(@Param("kw") String kw, Pageable pageable);
    //~3-13-9-1 쿼리 검색 기능
}