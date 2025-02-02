package reactpractice.back.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import reactpractice.back.entity.TestEntity;
import reactpractice.back.service.TestService;

@RestController
public class TestController {
    
    @Autowired
    private TestService testService;

    @PostMapping("/api/test")
    public void saveTestEntity(@RequestBody TestEntity testEntity){
        System.out.println(testEntity);
        testService.saveTestEntity(testEntity);
    }

    @GetMapping("/api/test")
    public List<TestEntity> getAllTestEntities(){
        return testService.getAllTestEntities();
    }
}
