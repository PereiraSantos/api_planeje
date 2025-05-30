package com.api.planeje.revision.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;


import com.api.planeje.revision.dao.RevisionRepository;
import com.api.planeje.revision.entity.Revision;

@Service
public class RevisionService {

    @Autowired
    private RevisionRepository revisionRepository;

    public List<Revision> GetRevision() {
        return revisionRepository.findAll();
    }

    public String saveRevision(Revision body) {
        Revision revision = new Revision();

        if (body.getId() != null) {
            revision.setId(body.getId());
        } else {
            Integer id = revisionRepository.lastId();
            id = id == null ? 1 : id + 1;

            revision.setId(id);
            revision.setDisable(0);
        }

        revision.setTitle(body.getTitle());
        revision.setDescription(body.getDescription());
        revision.setDateCreational(body.getDateCreational());
        revision.setIdRevisionTheme(body.getIdRevisionTheme());

        revisionRepository.save(revision);
        
        return body.getId() != null ? "Atualizado com succeso!!!" : "Salvo com succeso!!!";
    }

    public Revision getRevisivioById(Integer id) {
        return revisionRepository.getRevisionById(id);
    }

    public List<Revision> filterRevisionTitle(String title) {
        return revisionRepository.filterRevisionTitle(title);
    }

    public String updateRevisionById(Revision body){
        revisionRepository.updateRevisionById(body.getDisable(), body.getId());
        
        return  "Atualizado com succeso!!!";
    }
}
