import { Component } from '@angular/core';
import { Observable, of } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { Hero } from '../hero';
import { HeroService } from '../hero.service';

@Component({
  selector: 'app-hero-search',
  templateUrl: './hero-search.component.html',
  styleUrls: ['./hero-search.component.css'],
})
export class HeroSearchComponent {
  heroes: Observable<Hero[]> = of([]);

  constructor(private heroService: HeroService) {}

  searchHeroes(term: string): void {
    if (!term.trim()) {
      this.heroes = of([]);
      return;
    }
    this.heroes = this.heroService
      .searchHeroes(term)
      .pipe(catchError(this.handleError<Hero[]>('searchHeroes', [])));
  }

  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
      console.error(`${operation} failed: ${error.message}`);
      return of(result as T);
    };
  }
}
