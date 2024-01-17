package com.mysite.sbbPrj.question;

import java.time.LocalDateTime;
import java.util.List;

import jakarta.persistence.CascadeType;
import jakarta.persistence.Column;
import jakarta.persistence.Entity; 
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.OneToMany; 

import lombok.Getter;
import lombok.Setter;

import jakarta.persistence.ManyToOne;
import com.mysite.sbbPrj.user.SiteUser;
import java.util.Set;
import jakarta.persistence.ManyToMany;

import com.mysite.sbbPrj.answer.Answer;

//2-4-1 질문 엔티티 생성~
@Getter
@Setter
@Entity
public class Question {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(length = 200)
    private String subject;

    @Column(columnDefinition = "TEXT")
    private String content;

    private LocalDateTime createDate;
    //~2-4-1 질문 엔티티 생성
    
    //2-4-4 답변과 질문 연결~
    @OneToMany(mappedBy = "question", cascade = CascadeType.REMOVE) 
    private List<Answer> answerList;
    //~2-4-4 답변과 질문 연결
    
    //3-8-1 글쓴이 생성~
    @ManyToOne
    private SiteUser author;
    //~3-8-1 글쓴이 생성

    //3-9-1-1 수정 일시 추가
    private LocalDateTime modifyDate;
    
    //3-10-1-1 질문 엔티티 추가
    @ManyToMany
    Set<SiteUser> voter;

}