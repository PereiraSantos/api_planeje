package com.api.planeje.question.entity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Data;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Data
@Entity
@Table(name = "question")
public class Question {

    @Id
    private Integer id;

    @Column(name = "id_quiz")
    private Integer idQuiz;

    private String description;
    
    private Integer answer;

    private Integer disable;

}
