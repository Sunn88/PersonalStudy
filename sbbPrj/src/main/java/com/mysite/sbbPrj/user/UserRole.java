package com.mysite.sbbPrj.user;

import lombok.Getter;

//3-7-5 회원 권한 클래스
@Getter
public enum UserRole {
    ADMIN("ROLE_ADMIN"),
    USER("ROLE_USER");

    UserRole(String value) {
        this.value = value;
    }

    private String value;
}