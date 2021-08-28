import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {ActivatedRoute, Router} from '@angular/router';
import {tap} from 'rxjs/operators';
import {JwtHelperService} from '@auth0/angular-jwt';

const url = 'http://127.0.0.1:8000/api/user/';
const tokenurl = 'http://127.0.0.1:8000/auth/token/';
const refreshToken = 'http://127.0.0.1:8000/auth/token/refresh/';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  token: any;
  constructor(private httpClient: HttpClient, private router: Router, private route: ActivatedRoute) { }
  register(data): Observable<any>{
    return this.httpClient.post(url, data);
  }
  login(data): Observable<any>{
    const returnurl = this.route.snapshot.queryParams.returnurl || '/';
    localStorage.setItem('returnurl', returnurl);
    return this.httpClient.post(tokenurl, data);
  }
  loggedIn(): any{
    return !!localStorage.getItem('refresh');
  }
  logout(): void {
    localStorage.removeItem('refresh');
    localStorage.removeItem('access');
    this.router.navigate(['/login']);
  }
  getAccess(): any{
    return localStorage.getItem('access');
  }
  getRefresh(): any{
    return localStorage.getItem('refresh');
  }
  refreshToken(): any {
    return this.httpClient.post<any>(refreshToken, {
      refresh: this.getRefresh()
    }).pipe(tap((tokens: any) => {
      localStorage.setItem('access', tokens.access);
    }));
  }
  getUserInfo(): any{
    const helper = new JwtHelperService();
    const decodedToken = helper.decodeToken(this.getAccess());
    return decodedToken.user_id;
  }
}
