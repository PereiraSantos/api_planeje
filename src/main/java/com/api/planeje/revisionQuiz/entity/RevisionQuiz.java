package com.api.planeje.revisionQuiz.entity;

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
@Table(name = "revision_quiz")
public class RevisionQuiz {
    
    @Id
    private Integer id;

    private Integer answer;

    @Column(name="date_revision")
    private String dateRevision;
    
    @Column(name="id_quiz")
    private Integer idQuiz;

    private Integer disable;
}
