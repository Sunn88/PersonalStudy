package com.mysite.sbbPrj.user;

import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import java.util.Optional;
import com.mysite.sbbPrj.DataNotFoundException;

import lombok.RequiredArgsConstructor;

//3-6-3 회원 서비스 생성~
@RequiredArgsConstructor
@Service
public class UserService {

    private final UserRepository userRepository;
    //3-6-5-1 PasswordEncoder~
    private final PasswordEncoder passwordEncoder;
    //~3-6-5-1 PasswordEncoder

    public SiteUser create(String username, String email, String password) {
        SiteUser user = new SiteUser();
        user.setUsername(username);
        user.setEmail(email);
        //3-6-5-2 PasswordEncoder~
        user.setPassword(passwordEncoder.encode(password));
        //~3-6-5-2 PasswordEncoder
        this.userRepository.save(user);
        return user;
    }
    //~3-6-3 회원 서비스 생성 

    //3-8-4 사용자명으로 회원 조회~
    public SiteUser getUser(String username) {
        Optional<SiteUser> siteUser = this.userRepository.findByusername(username);
        if (siteUser.isPresent()) {
            return siteUser.get();
        } else {
            throw new DataNotFoundException("siteuser not found");
        }
    }
    //~3-8-4 사용자명으로 회원 조회
}