import { Component, OnInit } from '@angular/core';
import {ProjectService} from '../../services/project/project.service';
import {Observable} from 'rxjs';

@Component({
  selector: 'app-project-page',
  templateUrl: './project-page.component.html',
  styleUrls: ['./project-page.component.scss']
})
export class ProjectPageComponent implements OnInit {
  projects: any;
  tools: any;
  ProjectSource: Observable<any>;
  constructor(private projectService: ProjectService) {
  }

  ngOnInit(): void {
    this.projectService.readAll().subscribe(data => {
      this.projects = data;
    });
  }
  filterProject(str: string): any{
    const data = [];
    for (let project of this.projects) {
      for (let tools of project.tools_and_technology) {
        if (tools.name === str) {
          data.push(project);
        }
      }
      for (let tools of project.domain) {
        if (tools.name === str) {
          data.push(project);
        }
      }
      for (let tools of project.environment) {
        if (tools.name === str) {
          data.push(project);
        }
      }
    }
    if (data.length > 0){
      this.projects = data;
    }
    console.log(data);
    return data;
  }
  onTag(str: string): void{
    this.projectService.readAll().subscribe(data => {
      this.projects = data;
      this.tools = str;
      this.filterProject(str);
      console.log(str);
    });
  }

}
