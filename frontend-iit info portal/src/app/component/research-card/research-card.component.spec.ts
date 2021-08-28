import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ResearchCardComponent } from './research-card.component';

describe('ResearchCardComponent', () => {
  let component: ResearchCardComponent;
  let fixture: ComponentFixture<ResearchCardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ResearchCardComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ResearchCardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
