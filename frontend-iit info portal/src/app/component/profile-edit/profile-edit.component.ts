import { Component, OnInit } from '@angular/core';
import {FormControl, FormGroup, Validators} from '@angular/forms';
import {ProfileService} from '../../services/profile/profile.service';
import {Router} from '@angular/router';
import {AuthService} from '../../services/auth/auth.service';

@Component({
  selector: 'app-profile-edit',
  templateUrl: './profile-edit.component.html',
  styleUrls: ['./profile-edit.component.scss']
})
export class ProfileEditComponent implements OnInit {
  formGroup: FormGroup;
  photo: File;
  constructor(private profileService: ProfileService, private route: Router,
              private authService: AuthService) { }

  ngOnInit(): void {
    this.formGroup = new FormGroup({
      iit_program: new FormControl('', [Validators.required]),
      batch: new FormControl('', [Validators.required]),
      graduate_university: new FormControl('', [Validators.required]),
      is_current: new FormControl( '', [Validators.required]),
      additional_mail: new FormControl('', []),
      facebook: new FormControl('', []),
      github: new FormControl('', []),
      phone: new FormControl('', []),
      linkedIn: new FormControl('', []),
      college: new FormControl('', [Validators.required]),
    });
  }
  onFileChange(event): void {
    this.photo = event.target.files[0];
  }
  submit(): void {
    let formData = new FormData();
    let form = this.formGroup.getRawValue();
    // form.is_current = JSON.parse(form.is_current);
    form.user = this.authService.getUserInfo();
    formData.append('user', form.user);
    formData.append('iit_program', form.iit_program);
    formData.append('batch', form.batch);
    formData.append('is_current', form.is_current);
    formData.append('graduate_university', form.graduate_university);
    formData.append('additional_mail', form.additional_mail);
    formData.append('facebook', form.facebook);
    formData.append('github', form.github);
    formData.append('phone', form.phone);
    formData.append('linkedIn', form.linkedIn);
    formData.append('college', form.college);
    formData.append('photo', this.photo, this.photo.name);
    if (this.formGroup.valid)
    {
       this.profileService.create(formData)
        .subscribe(() => this.route.navigate(['/profile']));
     }
  }
}
