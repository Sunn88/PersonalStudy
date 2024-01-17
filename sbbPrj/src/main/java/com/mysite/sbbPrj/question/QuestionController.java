package com.mysite.sbbPrj.question;

import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import lombok.RequiredArgsConstructor;

import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import jakarta.validation.Valid;
import org.springframework.validation.BindingResult;
import com.mysite.sbbPrj.answer.AnswerForm;
import org.springframework.data.domain.Page;
import java.security.Principal;
import com.mysite.sbbPrj.user.SiteUser;
import com.mysite.sbbPrj.user.UserService;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.http.HttpStatus;
import org.springframework.web.server.ResponseStatusException;


//2-11 URL 프리픽스~
@RequestMapping("/question")
//~2-11 URL 프리픽스
@RequiredArgsConstructor
//2-7-1 질문 목록 URL 매핑~
@Controller
public class QuestionController {
	//2-7-4 데이터를 탬플릿에 전달~
	//2-9-2 컨트롤러에서 서비스 사용
	private final QuestionService questionService;
	//3-8-8-1
    private final UserService userService;
	
    @GetMapping("/list")
    //3-2-3 질문 페이징~
    //3-13-4-1 질문 검색 수정~
    public String list(Model model, @RequestParam(value="page", defaultValue="0") int page, @RequestParam(value = "kw", defaultValue = "") String kw) {
    	Page<Question> paging = this.questionService.getList(page, kw);
        //~3-13-4-1 질문 검색 수정
        model.addAttribute("paging", paging);
        //~3-2-3 질문 페이징
    	//~2-7-4 데이터를 탬플릿에 전달
        //3-13-4-2 질문 검색 수정~
        model.addAttribute("kw", kw);
        //~3-13-4-2 질문 검색 수정
        //2-7-3-2 탬플릿 매핑~
        return "question_list";
        //~2-7-3-2 탬플릿 매핑
    }
    //~2-7-1 질문 목록 URL 매핑
    
    //2-10-2 상세페이지 컨트롤러~
    //2-16-16 답변 폼 객체 전달~
    @GetMapping(value = "/detail/{id}")
    public String detail(Model model, @PathVariable("id") Integer id, AnswerForm answerForm) {
        //~	2-16-16 답변 폼 객체 전달
    	//2-10-5 Question 객체를 탬플릿에 전달~
    	Question question = this.questionService.getQuestion(id);
        model.addAttribute("question", question);
    	//~2-10-5 Question 객체를 탬플릿에 전달
        return "question_detail";
    }
    //~2-10-2 상세페이지 컨트롤러~
    
    //3-8-9-1 로그인했을때만 메서드 실행~
    @PreAuthorize("isAuthenticated()")
    //~3-8-9-1 로그인했을때만 메서드 실행
    //2-16-2 질문 등록 매핑~
    //2-16-11 질문 폼클래스 객체 사용~
    @GetMapping("/create")
    public String questionCreate(QuestionForm questionForm) {
        //~2-16-11 질문 폼클래스 객체 사용
        return "question_form";
    }
    //~2-16-2 질문 등록 매핑
    //3-8-9-2 로그인했을때만 메서드 실행~
    @PreAuthorize("isAuthenticated()")
    //~3-8-9-2 로그인했을때만 메서드 실행
    //2-16-4 질문 등록 post 요청~
    @PostMapping("/create")
    //2-16-9 질문 폼클래스 사용~
    //3-8-8-2~
    public String questionCreate(@Valid QuestionForm questionForm, BindingResult bindingResult, Principal principal) {
        //~3-8-8-2
    	if (bindingResult.hasErrors()) {
            return "question_form";
        }
        //3-8-8-3~
        SiteUser siteUser = this.userService.getUser(principal.getName());
        //~3-8-8-3
        //2-16-6 질문 등록 서비스 사용~
    	this.questionService.create(questionForm.getSubject(), questionForm.getContent(), siteUser);
        //~2-16-6 질문 등록 서비스 사용
        //~2-16-9 질문 폼클래스 사용
        return "redirect:/question/list"; // 질문 저장후 질문목록으로 이동
    }
    //~2-16-4 질문 등록 post 요청
    
    //3-9-3 질문 컨트롤러 수정~
    @PreAuthorize("isAuthenticated()")
    @GetMapping("/modify/{id}")
    public String questionModify(QuestionForm questionForm, @PathVariable("id") Integer id, Principal principal) {
        Question question = this.questionService.getQuestion(id);
        if(!question.getAuthor().getUsername().equals(principal.getName())) {
            throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "수정권한이 없습니다.");
        }
        questionForm.setSubject(question.getSubject());
        questionForm.setContent(question.getContent());
        return "question_form";
    }
    //~3-9-3 질문 컨트롤러 수정
    //3-9-6 질문 컨트롤러 수정~
    @PreAuthorize("isAuthenticated()")
    @PostMapping("/modify/{id}")
    public String questionModify(@Valid QuestionForm questionForm, BindingResult bindingResult, 
            Principal principal, @PathVariable("id") Integer id) {
        if (bindingResult.hasErrors()) {
            return "question_form";
        }
        Question question = this.questionService.getQuestion(id);
        if (!question.getAuthor().getUsername().equals(principal.getName())) {
            throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "수정권한이 없습니다.");
        }
        this.questionService.modify(question, questionForm.getSubject(), questionForm.getContent());
        return String.format("redirect:/question/detail/%s", id);
    }
    //~3-9-6 질문 컨트롤러 수정
    
    //3-9-11 질문 삭제 컨트롤러~
    @PreAuthorize("isAuthenticated()")
    @GetMapping("/delete/{id}")
    public String questionDelete(Principal principal, @PathVariable("id") Integer id) {
        Question question = this.questionService.getQuestion(id);
        if (!question.getAuthor().getUsername().equals(principal.getName())) {
            throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "삭제권한이 없습니다.");
        }
        this.questionService.delete(question);
        return "redirect:/";
    }
    //~3-9-11 질문 삭제 컨트롤러
    
    //3-10-2-4 추천 버튼 URL 처리~
    @PreAuthorize("isAuthenticated()")
    @GetMapping("/vote/{id}")
    public String questionVote(Principal principal, @PathVariable("id") Integer id) {
        Question question = this.questionService.getQuestion(id);
        SiteUser siteUser = this.userService.getUser(principal.getName());
        this.questionService.vote(question, siteUser);
        return String.format("redirect:/question/detail/%s", id);
    }
    //~3-10-2-4 추천 버튼 URL 처리
    
}