package com.mysite.sbbPrj.answer;

import java.time.LocalDateTime;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.ManyToOne;
import lombok.Getter;
import lombok.Setter;

import com.mysite.sbbPrj.question.Question;

import com.mysite.sbbPrj.user.SiteUser;
import java.util.Set;
import jakarta.persistence.ManyToMany;

//2-4-2 답변 엔티티 생성~
@Getter
@Setter
@Entity
public class Answer {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(columnDefinition = "TEXT")
    private String content;

    private LocalDateTime createDate; 

    //2-4-3 질문과 답변 연결~
    @ManyToOne
    //~2-4-3 질문과 답변 연결
    private Question question; 
    //~2-4-2 질문 엔티티 생성
    
    //3-8-2 글쓴이 생성~
    @ManyToOne
    private SiteUser author;
    //~3-8-2 글쓴이 생성

    //3-9-1-2 수정 일시 추가
    private LocalDateTime modifyDate;
    
    //3-10-1-2 답변 엔티티 추가
    @ManyToMany
    Set<SiteUser> voter;
}