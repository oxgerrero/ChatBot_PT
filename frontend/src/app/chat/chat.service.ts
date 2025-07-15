import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';

@Injectable({ providedIn: 'root' })
export class ChatService {
  private sessionId = this.getSessionId();
  private apiUrl = `${environment.apiUrl}/answer`;

  constructor(private http: HttpClient) {}

  private getSessionId(): string {
    const key = 'chat_session_id';
    const existing = localStorage.getItem(key);
    if (existing) return existing;

    const newId = crypto.randomUUID();
    localStorage.setItem(key, newId);
    return newId;
  }

  async sendQuestion(question: string): Promise<any> {
    const body = {
      question,
      session_id: this.sessionId
    };

    const response = await this.http.post<any>(this.apiUrl, body).toPromise();

    return {
      role: 'assistant',
      content: response.answer,
      timestamp: new Date(),
      sources: response.sources
    };
  }
}
