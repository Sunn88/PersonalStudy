package com.mysite.sbbPrj.answer;

import com.mysite.sbbPrj.question.Question;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import java.time.LocalDateTime;
import com.mysite.sbbPrj.user.SiteUser;
import java.util.Optional;
import com.mysite.sbbPrj.DataNotFoundException;


//2-12-3 답변 서비스~
@RequiredArgsConstructor
@Service
public class AnswerService {

    private final AnswerRepository answerRepository;
    
    //3-8-5-1 답변 저장 시 글쓴이 저장~
    //3-11-2 답변 서비스 수정~
    public Answer create(Question question, String content, SiteUser author) {
        //~3-8-5-1 답변 저장 시 글쓴이 저장
        Answer answer = new Answer();
        answer.setContent(content);
        answer.setCreateDate(LocalDateTime.now());
        answer.setQuestion(question);
        //3-8-5-2 답변 저장 시 글쓴이 저장~
        answer.setAuthor(author);
        //~3-8-5-2 답변 저장 시 글쓴이 저장
        this.answerRepository.save(answer);
        return answer;
        //~3-11-2 답변 서비스 수정
    }
  //~2-12-3 답변 서비스
    
    //3-9-13 답변 조회 및 수정 서비스~
    public Answer getAnswer(Integer id) {
        Optional<Answer> answer = this.answerRepository.findById(id);
        if (answer.isPresent()) {
            return answer.get();
        } else {
            throw new DataNotFoundException("answer not found");
        }
    }

    public void modify(Answer answer, String content) {
        answer.setContent(content);
        answer.setModifyDate(LocalDateTime.now());
        this.answerRepository.save(answer);
    }
    //~3-9-13 답변 조회 및 수정 서비스
    
    //3-9-18 답변 삭제 서비스~
    public void delete(Answer answer) {
        this.answerRepository.delete(answer);
    }
    //~3-9-18 답변 삭제 서비스
    
    //3-10-3-2 답변 추천자 저장~
    public void vote(Answer answer, SiteUser siteUser) {
        answer.getVoter().add(siteUser);
        this.answerRepository.save(answer);
    }
    //~3-10-3-2 답변 추천자 저장
}