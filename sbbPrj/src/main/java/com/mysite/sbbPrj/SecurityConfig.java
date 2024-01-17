package com.mysite.sbbPrj;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.web.util.matcher.AntPathRequestMatcher;
import org.springframework.security.web.header.writers.frameoptions.XFrameOptionsHeaderWriter;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.config.annotation.authentication.configuration.AuthenticationConfiguration;
import org.springframework.security.config.annotation.method.configuration.EnableMethodSecurity;


//3-5-2 스프링 시큐리티 설정~
@Configuration
@EnableWebSecurity
//3-8-9-4 PreAuthorize 동작~
@EnableMethodSecurity(prePostEnabled = true)
//~3-8-9-4 PreAuthorize 동작
public class SecurityConfig {
    @Bean
    SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .authorizeHttpRequests((authorizeHttpRequests) -> authorizeHttpRequests
                .requestMatchers(new AntPathRequestMatcher("/**")).permitAll())
            //3-5-3 스프링 시큐리티가 CSRF 처리 시 H2 콘솔은 예외로 처리~
            .csrf((csrf) -> csrf
                    .ignoringRequestMatchers(new AntPathRequestMatcher("/h2-console/**")))
            //~3-5-3 스프링 시큐리티가 CSRF 처리 시 H2 콘솔은 예외로 처리
            //3-5-4 프레임 오류 수정~
            .headers((headers) -> headers
                    .addHeaderWriter(new XFrameOptionsHeaderWriter(
                        XFrameOptionsHeaderWriter.XFrameOptionsMode.SAMEORIGIN)))
            //~3-5-4 프레임 오류 수정
            //3-7-1 로그인 URL 등록~
            .formLogin((formLogin) -> formLogin
                    .loginPage("/user/login")
                    .defaultSuccessUrl("/"))
            //~3-7-1 로그인 URL 등록
            //3-7-10 로그아웃 기능~
            .logout((logout) -> logout
                    .logoutRequestMatcher(new AntPathRequestMatcher("/user/logout"))
                    .logoutSuccessUrl("/")
                    .invalidateHttpSession(true))
            //~3-7-10 로그아웃 기능
        ;
        return http.build();
    }
  //~3-5-2 스프링 시큐리티 설정
    
    //3-6-4 PasswordEncoder Bean~
    @Bean
    PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
    //~3-6-4 PasswordEncoder Bean
    
    //3-7-7 스프링 시큐리티 설정 수정
    @Bean
    AuthenticationManager authenticationManager(AuthenticationConfiguration authenticationConfiguration) throws Exception {
        return authenticationConfiguration.getAuthenticationManager();
    }
}