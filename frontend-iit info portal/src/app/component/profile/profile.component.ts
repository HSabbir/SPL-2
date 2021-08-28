import { Component, OnInit } from '@angular/core';
import {ProfileService} from '../../services/profile/profile.service';
import {ActivatedRoute} from '@angular/router';
import {ProjectService} from '../../services/project/project.service';
import {ResearchService} from '../../services/research/research.service';
import {HigherstudyService} from '../../services/higherStudies/higherstudy.service';
import {AuthService} from '../../services/auth/auth.service';
import {map} from 'rxjs/operators';
import {ProfessionService} from '../../services/profession/profession.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {
  profile: any;
  tempProfile: any;
  project: any;
  research: any;
  higherStudy: any;
  name: any;
  temProfession: any;
  toggleProject = false;
  constructor(private profileService: ProfileService,
              private route: ActivatedRoute,
              private projectService: ProjectService,
              private researchService: ResearchService,
              private higherstudyService: HigherstudyService,
              private authService: AuthService,
              private professionService: ProfessionService) {
  }

  ngOnInit(): void {
    this.profileService.readAll().pipe (map(items =>
      items.filter(item => item.user.id  === this.authService.getUserInfo())) ).subscribe(
      data => {
        this.profile = data[0];
        console.log(this.profile);
      }
    );
    const id = +this.route.snapshot.paramMap.get('profile');
    if (id) {
      this.profileService.readCompleteProfile(id).subscribe(data => {
        this.profile = data;
        this.name = this.profile.user.name ;
      });
    }
    this.projectService.readAll().subscribe(data => {
      this.project = data;
    });
    this.researchService.readAll().subscribe(data => {
      this.research = data;
    });
    this.higherstudyService.readAll().subscribe(data => {
      this.higherStudy = data;
    });
    this.professionService.readAll().subscribe(data => {
      this.temProfession = data;
    });
  }
  filterProject(id: number): any{
    const data = [];
    for (let project of this.project) {
      for (let user of project.user) {
        if (user.id === id) {
          data.push(project);
        }
      }
    }
    if (data.length === 0){
      return false;
    }
    return data;
  }
  filterProfile(id: number): any{
    for (const profile of this.tempProfile) {
      if (profile.user.id === id) {
        return profile;
      }
    }
    return false;
  }
  filterProfession(id: number): any{
    const data = [];
    for (const profession of this.temProfession) {
      if (profession.user.id === id) {
        data.push(profession) ;
      }
    }
    if (data.length === 0){
      return false;
    }
    return data;
  }
  filterResearch(id: number): any{
    const data = [];
    for (let research of this.research) {
        if (research.user.id === id) {
          data.push(research);
      }
    }
    if (data.length === 0){
      return false;
    }
    return data;
  }
  filterHigherStdy(id: number): any{
    const data = [];
    for (let study of this.higherStudy) {
      if (study.user.id === id) {
        data.push(study);
      }
    }
    if (data.length === 0){
      return false;
    }
    return data;
  }
}
