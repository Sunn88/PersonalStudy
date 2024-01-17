package com.mysite.sbbPrj.answer;

import com.mysite.sbbPrj.question.Question;
import com.mysite.sbbPrj.question.QuestionService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import jakarta.validation.Valid;
import org.springframework.validation.BindingResult;
import java.security.Principal;
import com.mysite.sbbPrj.user.SiteUser;
import com.mysite.sbbPrj.user.UserService;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.server.ResponseStatusException;

//2-12-2 답변 컨트롤러~
@RequestMapping("/answer")
@RequiredArgsConstructor
@Controller
public class AnswerController {

    private final QuestionService questionService;
    //2-12-4 답변 서비스 사용~
    private final AnswerService answerService;
    //3-8-6-1
    private final UserService userService;

    //3-8-9-3 로그인했을때만 메서드 실행~
    @PreAuthorize("isAuthenticated()")
    //~3-8-9-1 로그인했을때만 메서드 실행
    @PostMapping("/create/{id}")
    //2-16-14 답변 폼클래스 사용~
    //3-8-3 사용자 정보 저장~
    public String createAnswer(Model model, @PathVariable("id") Integer id,  @Valid AnswerForm answerForm, BindingResult bindingResult, Principal principal) {
        //~3-8-3 사용자 정보 저장
        Question question = this.questionService.getQuestion(id);
        //3-8-6-2~
        SiteUser siteUser = this.userService.getUser(principal.getName());
        //~3-8-6-2
        if (bindingResult.hasErrors()) {
            model.addAttribute("question", question);
            return "question_detail";
        }
        //3-8-6-3~
        //3-11-3-1 답변 컨트롤러 앵커 추가~
        Answer answer = this.answerService.create(question, 
                answerForm.getContent(), siteUser);
        //~3-8-6-3
        //~2-16-14 답변 폼클래스 사용
        //~2-12-4 답변 서비스 사용
        return String.format("redirect:/question/detail/%s#answer_%s", 
                answer.getQuestion().getId(), answer.getId());
        //~3-11-3-1 답변 컨트롤러 앵커 추가
    }
    //~2-12-2 답변 컨트롤러
    
    //3-9-14 답변 수정 컨트롤러~
    @PreAuthorize("isAuthenticated()")
    @GetMapping("/modify/{id}")
    public String answerModify(AnswerForm answerForm, @PathVariable("id") Integer id, Principal principal) {
        Answer answer = this.answerService.getAnswer(id);
        if (!answer.getAuthor().getUsername().equals(principal.getName())) {
            throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "수정권한이 없습니다.");
        }
        answerForm.setContent(answer.getContent());
        return "answer_form";
    }
    //~3-9-14 답변 수정 컨트롤러
    //3-9-16 답변 컨트롤러 재수정~
    @PreAuthorize("isAuthenticated()")
    @PostMapping("/modify/{id}")
    public String answerModify(@Valid AnswerForm answerForm, BindingResult bindingResult,
            @PathVariable("id") Integer id, Principal principal) {
        if (bindingResult.hasErrors()) {
            return "answer_form";
        }
        Answer answer = this.answerService.getAnswer(id);
        if (!answer.getAuthor().getUsername().equals(principal.getName())) {
            throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "수정권한이 없습니다.");
        }
        this.answerService.modify(answer, answerForm.getContent());
        //3-11-3-2 답변 컨트롤러 앵커 추가~
        return String.format("redirect:/question/detail/%s#answer_%s", 
                answer.getQuestion().getId(), answer.getId());
        //~3-11-3-2 답변 컨트롤러 앵커 추가
    }
    //~3-9-16 답변 컨트롤러 재수정
    
    //3-9-19 답변 삭제 컨트롤러~
    @PreAuthorize("isAuthenticated()")
    @GetMapping("/delete/{id}")
    public String answerDelete(Principal principal, @PathVariable("id") Integer id) {
        Answer answer = this.answerService.getAnswer(id);
        if (!answer.getAuthor().getUsername().equals(principal.getName())) {
            throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "삭제권한이 없습니다.");
        }
        this.answerService.delete(answer);
        return String.format("redirect:/question/detail/%s", answer.getQuestion().getId());
    }
    //~3-9-19 답변 삭제 컨트롤러
    
    //3-10-3-3 답변 추천 URL 처리~
    @PreAuthorize("isAuthenticated()")
    @GetMapping("/vote/{id}")
    public String answerVote(Principal principal, @PathVariable("id") Integer id) {
        Answer answer = this.answerService.getAnswer(id);
        SiteUser siteUser = this.userService.getUser(principal.getName());
        this.answerService.vote(answer, siteUser);
        //3-11-3-3 답변 컨트롤러 앵커 추가~
        return String.format("redirect:/question/detail/%s#answer_%s", 
                answer.getQuestion().getId(), answer.getId());
        //~3-11-3-3 답변 컨트롤러 앵커 추가
    }
    //~3-10-3-3 답변 추천 URL 처리
    
}