import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { MdbModule } from 'mdb-angular-ui-kit';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NavbarComponent } from './component/navbar/navbar.component';
import {HTTP_INTERCEPTORS, HttpClientModule} from '@angular/common/http';
// import {MatLinkPreviewModule} from '@angular-material-extensions/link-preview';

import {RouterModule} from '@angular/router';
import { HomePageComponent } from './component/home-page/home-page.component';
import { PeopleComponent } from './component/people/people.component';
import { SinglePeopleComponent } from './component/single-people/single-people.component';
import { ProjectPageComponent } from './component/project-page/project-page.component';
import { SingleProjectComponent } from './component/single-project/single-project.component';
import { ProfileComponent } from './component/profile/profile.component';
import { ProfessionCardsComponent } from './component/profession-cards/profession-cards.component';
import { LoginComponent } from './component/login/login.component';
import { RegisterComponent } from './component/register/register.component';
import { ProfileEditComponent } from './component/profile-edit/profile-edit.component';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {AuthGuardGuard} from './guard/auth/auth-guard.guard';
import {AuthService} from './services/auth/auth.service';
import {InterceptorService} from './services/token_interceptor/interceptor.service';
import { ResearchCardComponent } from './component/research-card/research-card.component';
import { HigherStudyCardComponent } from './component/higher-study-card/higher-study-card.component';
import { CreteItemComponent } from './component/crete-item/crete-item.component';
import { AdminComponent } from './component/admin/admin.component';

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    HomePageComponent,
    PeopleComponent,
    SinglePeopleComponent,
    ProjectPageComponent,
    SingleProjectComponent,
    ProfileComponent,
    ProfessionCardsComponent,
    LoginComponent,
    RegisterComponent,
    ProfileEditComponent,
    ResearchCardComponent,
    HigherStudyCardComponent,
    CreteItemComponent,
    AdminComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    MdbModule,
    BrowserAnimationsModule,
    RouterModule.forRoot([
      {path: 'login', component: LoginComponent},
      {path: 'register', component: RegisterComponent},
      {path: '', component: HomePageComponent, canActivate: [AuthGuardGuard]},
      {path: 'people', component: PeopleComponent, canActivate: [AuthGuardGuard]},
      {path: 'project', component: ProjectPageComponent, canActivate: [AuthGuardGuard]},
      {path: 'profile', component: ProfileComponent, canActivate: [AuthGuardGuard]},
      {path: 'people/:profile', component: ProfileComponent, canActivate: [AuthGuardGuard]},
      {path: 'profile_create', component: ProfileEditComponent, canActivate: [AuthGuardGuard]},
      // {path: 'order', component: OrderFormComponent, canActivate: [AuthGuard]},
      // {path: 'allorder', component: ShowAllOrderComponent, canActivate: [AuthGuard]},
      {path: 'admin', component: AdminComponent}
    ]),
    // MatLinkPreviewModule,
    FormsModule,
    ReactiveFormsModule,
  ],
  providers: [AuthService, AuthGuardGuard,
    { provide: HTTP_INTERCEPTORS, useClass: InterceptorService, multi: true }],
  bootstrap: [AppComponent]
})
export class AppModule { }
