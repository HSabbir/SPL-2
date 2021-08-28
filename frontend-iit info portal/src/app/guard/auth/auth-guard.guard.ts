import { Injectable } from '@angular/core';
import {CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, UrlTree, Router} from '@angular/router';
import { Observable } from 'rxjs';
import {AuthService} from '../../services/auth/auth.service';

@Injectable({
  providedIn: 'root'
})
export class AuthGuardGuard implements CanActivate {
  constructor(private authservice: AuthService,
              private router: Router) {
  }
  canActivate(route, state: RouterStateSnapshot): boolean {
    if (this.authservice.loggedIn()){
      return true;
    }else {
      this.router.navigate(['/login'], {queryParams: {returnurl: state.url}});
      return false;
    }
  }
}
