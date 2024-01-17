package com.mysite.sbbPrj;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import com.mysite.sbbPrj.question.QuestionService;

@SpringBootTest
class SbbPrjApplicationTests {
	//2-5-4 질문 데이터 저장~
//	@Autowired
//    private QuestionRepository questionRepository;
//
//    @Test
//    void testJpa() {        
//        Question q1 = new Question();
//        q1.setSubject("sbb가 무엇인가요?");
//        q1.setContent("sbb에 대해서 알고 싶습니다.");
//        q1.setCreateDate(LocalDateTime.now());
//        this.questionRepository.save(q1);  // 첫번째 질문 저장
//
//        Question q2 = new Question();
//        q2.setSubject("스프링부트 모델 질문입니다.");
//        q2.setContent("id는 자동으로 생성되나요?");
//        q2.setCreateDate(LocalDateTime.now());
//        this.questionRepository.save(q2);  // 두번째 질문 저장
//    }
	//~2-5-4 질문 데이터 저장
	
	//2-5-5 findAll 메소드~
//    @Test
//    void testJpa() {
//        List<Question> all = this.questionRepository.findAll();
//        assertEquals(2, all.size());
//
//        Question q = all.get(0);
//        assertEquals("sbb가 무엇인가요?", q.getSubject());
//    }
	//~2-5-5 findAll 메소드
	
	//2-5-6 findById 메소드~
//    @Test
//    void testJpa() {
//        Optional<Question> oq = this.questionRepository.findById(1);
//        if(oq.isPresent()) {
//            Question q = oq.get();
//            assertEquals("sbb가 무엇인가요?", q.getSubject());
//        }
//    }
	//~2-5-6 findById 메소드
	
	//2-5-7-2 findBySubject 메소드~
//	@Test
//    void testJpa() {
//        Question q = this.questionRepository.findBySubject("sbb가 무엇인가요?");
//        assertEquals(1, q.getId());
//    }
	//~2-5-7-2 findBySubject 메소드
	
	//2-5-9-2 findBySubjectAndContent 메소드~
//	@Test
//    void testJpa() {
//        Question q = this.questionRepository.findBySubjectAndContent(
//                "sbb가 무엇인가요?", "sbb에 대해서 알고 싶습니다.");
//        assertEquals(1, q.getId());
//    }
	//~2-5-9-2 findBySubjectAndContent 메소드
	
	//2-5-10-2 findBySubjectLike 메소드~
//	@Test
//    void testJpa() {
//        List<Question> qList = this.questionRepository.findBySubjectLike("sbb%");
//        Question q = qList.get(0);
//        assertEquals("sbb가 무엇인가요?", q.getSubject());
//    }
	//~2-5-10-2 findBySubjectLike 메소드
	
	//2-5-11 질문 데이터 수정~
//	@Test
//    void testJpa() {
//        Optional<Question> oq = this.questionRepository.findById(1);
//        assertTrue(oq.isPresent());
//        Question q = oq.get();
//        q.setSubject("수정된 제목");
//        this.questionRepository.save(q);
//    }
	//~2-5-11 질문 데이터 수정
	
	//2-5-12 질문 데이터 삭제~
//	@Test
//    void testJpa() {
//        assertEquals(2, this.questionRepository.count());
//        Optional<Question> oq = this.questionRepository.findById(1);
//        assertTrue(oq.isPresent());
//        Question q = oq.get();
//        this.questionRepository.delete(q);
//        assertEquals(1, this.questionRepository.count());
//    }
	//~2-5-12 질문 데이터 삭제
	
	//2-5-13 답변 데이터 저장~
//	@Autowired
//    private AnswerRepository answerRepository;
//
//    @Test
//    void testJpa() {
//        Optional<Question> oq = this.questionRepository.findById(2);
//        assertTrue(oq.isPresent());
//        Question q = oq.get();
//
//        Answer a = new Answer();
//        a.setContent("네 자동으로 생성됩니다.");
//        a.setQuestion(q);  // 어떤 질문의 답변인지 알기위해서 Question 객체가 필요하다.
//        a.setCreateDate(LocalDateTime.now());
//        this.answerRepository.save(a);
//    }
	//~2-5-13 답변 데이터 저장
	
	//2-5-14 답변 데이터 조회~
//	@Test
//    void testJpa() {
//        Optional<Answer> oa = this.answerRepository.findById(1);
//        assertTrue(oa.isPresent());
//        Answer a = oa.get();
//        assertEquals(2, a.getQuestion().getId());
//    }
	//~2-5-14 답변 데이터 조회
	
	//2-5-15 질문 데이터에 연결된 답변 데이터 찾기~
//	@Transactional
//		@Test
//    void testJpa() {
//        Optional<Question> oq = this.questionRepository.findById(2);
//        assertTrue(oq.isPresent());
//        Question q = oq.get();
//
//        List<Answer> answerList = q.getAnswerList();
//
//        assertEquals(1, answerList.size());
//        assertEquals("네 자동으로 생성됩니다.", answerList.get(0).getContent());
//    }
	//~2-5-15 질문 데이터에 연결된 답변 데이터 찾기

	//3-1-2 페이징 테스트~
	 @Autowired
	 private QuestionService questionService;

    @Test
    void testJpa() {
        for (int i = 1; i <= 300; i++) {
            String subject = String.format("테스트 데이터입니다:[%03d]", i);
            String content = "내용무";
            this.questionService.create(subject, content, null);
        }
    }
	//~3-1-2 페이징 테스트
}
