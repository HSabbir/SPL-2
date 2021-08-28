import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HigherStudyCardComponent } from './higher-study-card.component';

describe('HigherStudyCardComponent', () => {
  let component: HigherStudyCardComponent;
  let fixture: ComponentFixture<HigherStudyCardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ HigherStudyCardComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(HigherStudyCardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
