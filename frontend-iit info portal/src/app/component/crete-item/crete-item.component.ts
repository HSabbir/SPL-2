import { Component, OnInit } from '@angular/core';
import {ProjectService} from '../../services/project/project.service';
import {FormControl, FormGroup, Validators} from '@angular/forms';
import {AuthService} from '../../services/auth/auth.service';
import {ActivatedRoute, Route} from '@angular/router';
import {ResearchService} from '../../services/research/research.service';
import {ProfessionService} from '../../services/profession/profession.service';

@Component({
  selector: 'app-crete-item',
  templateUrl: './crete-item.component.html',
  styleUrls: ['./crete-item.component.scss']
})
export class CreteItemComponent implements OnInit {
  toogleProject = false;
  toogleResearch = false;
  toogleHigherStudy = false;
  toogleProfession = false;
  domains: any;
  environment: any;
  technology: any;
  formGroup: FormGroup;
  researchForm: FormGroup;
  professionForm: FormGroup;
  photo: File;
  selected = [];
  selected2 = [];
  selected3 = [];
  constructor(private projectService: ProjectService,
              private authService: AuthService,
              private researchService: ResearchService,
              private professionService: ProfessionService
              ) { }

  ngOnInit(): void {
    this.projectService.readAllDOmain().subscribe(data => {
      this.domains = data ;
    });
    this.projectService.readAllEnvironment().subscribe(data => {
      this.environment = data ;
    });
    this.projectService.readAllTechnology().subscribe(data => {
      this.technology = data ;
    });
    this.formGroup = new FormGroup({
      title: new FormControl('', [Validators.required]),
      domain: new FormControl('', [Validators.required]),
      environment: new FormControl('', [Validators.required]),
      tools_and_technology: new FormControl( '', [Validators.required]),
    });
    this.researchForm = new FormGroup({
      title: new FormControl('', [Validators.required]),
      research_domain: new FormControl('', [Validators.required]),
    });
    this.professionForm = new FormGroup({
      designation: new FormControl('', [Validators.required]),
      organization_name: new FormControl('', [Validators.required]),
      organization_type: new FormControl('', [Validators.required]),
      date_join: new FormControl('', [Validators.required]),
      url: new FormControl('', ),

    });
  }
  onFileChange(event): void {
    this.photo = event.target.files[0];
  }
  submitProject(): void {
    let formData = new FormData();
    let form = this.formGroup.getRawValue();
    console.log(form);
    // form.is_current = JSON.parse(form.is_current);
    form.user = this.authService.getUserInfo();
    formData.append('user', form.user);
    formData.append('title', form.title);
    formData.append('domain', form.domain);
    formData.append('tools_and_technology', form.tools_and_technology);
    formData.append('environment', form.environment);
    formData.append('photo', this.photo, this.photo.name);
    var object = {};
    formData.forEach((value, key) => object[key] = value);
    var json = JSON.stringify(object);
    if (this.formGroup.valid) {
      this.projectService.create(json)
        .subscribe(data => {
          this.changeProjectToggle('P');
          this.selected = [];
          this.selected2 = [];
          this.selected3 = [];
        });
    }
  }
  submitResearch(): void {
    const form = this.researchForm.getRawValue();
    form.user = this.authService.getUserInfo();
    if (this.researchForm.valid) {
      this.researchService.create(form)
        .subscribe(data => {
          console.log('done');
        });
    }
  }
  submitProfession(): void {
    const form = this.professionForm.getRawValue();
    form.user = this.authService.getUserInfo();
    console.log(form);
    if (this.professionForm.valid) {
      this.professionService.create(form)
        .subscribe(data => {
          console.log('done');
        });
    }
  }
  changeProjectToggle(str: string): void {
    if (str === 'P'){
      this.toogleProject = !this.toogleProject;
    }
    else if (str === 'R'){
      this.toogleResearch = !this.toogleResearch;
    }
    else if (str === 'H'){
      this.toogleHigherStudy = !this.toogleHigherStudy;
    }
    else{
      this.toogleProfession = !this.toogleProfession;
    }
  }
}
