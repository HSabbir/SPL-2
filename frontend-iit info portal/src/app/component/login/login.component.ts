import { Component, OnInit } from '@angular/core';
import {AuthService} from '../../services/auth/auth.service';
import {Router} from '@angular/router';
import {FormControl, FormGroup, Validators} from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  formGroup: FormGroup;
  constructor(private authService: AuthService, private router: Router) { }

  ngOnInit(): void {
    this.initForm();
  }
  initForm(): void {
    this.formGroup = new FormGroup({
      email: new FormControl('', [Validators.required]),
      password: new FormControl('', [Validators.required])
    });
  }
  loginProcess(): void {
    if (this.formGroup.valid){
      this.authService.login(this.formGroup.value).subscribe(result => {
        if (result.access){
          localStorage.setItem('refresh', result.refresh);
          localStorage.setItem('access', result.access);
          const url = localStorage.getItem('returnurl');
          this.router.navigateByUrl(url);
        }
      });
    }
  }
}
