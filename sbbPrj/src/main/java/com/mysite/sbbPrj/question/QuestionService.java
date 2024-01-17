package com.mysite.sbbPrj.question;

import java.util.List;

import org.springframework.stereotype.Service;

import lombok.RequiredArgsConstructor;

import java.util.Optional;
import com.mysite.sbbPrj.DataNotFoundException;
import java.time.LocalDateTime;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import java.util.ArrayList;
import java.util.List;
import org.springframework.data.domain.Sort;
import com.mysite.sbbPrj.user.SiteUser;
import com.mysite.sbbPrj.answer.Answer;
import jakarta.persistence.criteria.CriteriaBuilder;
import jakarta.persistence.criteria.CriteriaQuery;
import jakarta.persistence.criteria.Join;
import jakarta.persistence.criteria.JoinType;
import jakarta.persistence.criteria.Predicate;
import jakarta.persistence.criteria.Root;
import org.springframework.data.jpa.domain.Specification;

//2-9-1 서비스 생성~
@RequiredArgsConstructor
@Service
public class QuestionService {

    private final QuestionRepository questionRepository;

    public List<Question> getList() {
        return this.questionRepository.findAll();
    }
    //~2-9-1 서비스 생성
    
    //2-10-3 상세페이지 서비스 사용~
    public Question getQuestion(Integer id) {  
        Optional<Question> question = this.questionRepository.findById(id);
        if (question.isPresent()) {
            return question.get();
        } else {
            throw new DataNotFoundException("question not found");
        }
    }
    //~	2-10-3 상세페이지 서비스 사용
    
    //2-16-5 질문 등록 서비스~
    //3-8-7-1~
    public void create(String subject, String content, SiteUser user) {
        //~3-8-7-1
        Question q = new Question();
        q.setSubject(subject);
        q.setContent(content);
        q.setCreateDate(LocalDateTime.now());
        //3-8-7-2~
        q.setAuthor(user);
        //~3-8-7-2
        this.questionRepository.save(q);
    }
    //~2-16-5 질문 등록 서비스
    
    //3-2-2 질문 페이징~
    //3-13-3-1 질문 검색 수정~
    public Page<Question> getList(int page, String kw) {
        //~3-13-3-1 질문 검색 수정
    	//3-2-8 최신순 데이터 조회~
    	List<Sort.Order> sorts = new ArrayList<>();
        sorts.add(Sort.Order.desc("createDate"));
        Pageable pageable = PageRequest.of(page, 10, Sort.by(sorts));
        //3-13-3-2 질문 검색 수정~
        Specification<Question> spec = search(kw);
        //~3-13-3-2 질문 검색 수정
    	//~3-2-8 최신순 데이터 조회
        //3-13-3-3 질문 검색 수정~
        //3-13-9-2 쿼리 검색 수정~
        return this.questionRepository.findAllByKeyword(kw, pageable);
        //~3-13-9-2 쿼리 검색 수정
        //~3-13-3-3 질문 검색 수정
    }
    //~3-2-2 질문 페이징
    
    //3-9-5 질문 서비스 수정~
    public void modify(Question question, String subject, String content) {
        question.setSubject(subject);
        question.setContent(content);
        question.setModifyDate(LocalDateTime.now());
        this.questionRepository.save(question);
    }
    //~3-9-5 질문 서비스 수정
    
    //3-9-10 질문 삭제 서비스~
    public void delete(Question question) {
        this.questionRepository.delete(question);
    }
    //~3-9-10 질문 삭제 서비스
    
    //3-10-2-3 추천인 저장 기능~
    public void vote(Question question, SiteUser siteUser) {
        question.getVoter().add(siteUser);
        this.questionRepository.save(question);
    }
    //~3-10-2-3 추천인 저장 기능
    
    //3-13-1 검색 기능 서비스~
    private Specification<Question> search(String kw) {
        return new Specification<>() {
            private static final long serialVersionUID = 1L;
            @Override
            public Predicate toPredicate(Root<Question> q, CriteriaQuery<?> query, CriteriaBuilder cb) {
                query.distinct(true);  // 중복을 제거 
                Join<Question, SiteUser> u1 = q.join("author", JoinType.LEFT);
                Join<Question, Answer> a = q.join("answerList", JoinType.LEFT);
                Join<Answer, SiteUser> u2 = a.join("author", JoinType.LEFT);
                return cb.or(cb.like(q.get("subject"), "%" + kw + "%"), // 제목 
                        cb.like(q.get("content"), "%" + kw + "%"),      // 내용 
                        cb.like(u1.get("username"), "%" + kw + "%"),    // 질문 작성자 
                        cb.like(a.get("content"), "%" + kw + "%"),      // 답변 내용 
                        cb.like(u2.get("username"), "%" + kw + "%"));   // 답변 작성자 
            }
        };
    }
    //~3-13-1 검색 기능 서비스
    
}