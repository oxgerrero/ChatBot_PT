import { Component, OnInit } from '@angular/core';
import { ChatService } from './chat.service';

interface Message {
  role: 'user' | 'assistant';
  content: string;
  timestamp: Date;
  sources?: number[];
}

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css']
})
export class ChatComponent implements OnInit {
  messages: Message[] = [];
  userInput = '';
  loading = false;

  constructor(private chatService: ChatService) {}

  ngOnInit(): void {
    this.addSystemMessage('👋 ¡Hola! Estoy listo para ayudarte con tus preguntas sobre impuestos de renta.');
  }

  addSystemMessage(content: string) {
    this.messages.push({
      role: 'assistant',
      content,
      timestamp: new Date()
    });
  }

  async sendMessage() {
    if (!this.userInput.trim()) return;

    const userMessage: Message = {
      role: 'user',
      content: this.userInput,
      timestamp: new Date()
    };
    this.messages.push(userMessage);
    const input = this.userInput;
    this.userInput = '';
    this.loading = true;

    try {
      const response = await this.chatService.sendQuestion(input);
      this.messages.push(response);
    } catch (err) {
      this.messages.push({
        role: 'assistant',
        content: '❌ Error al conectar con el servidor.',
        timestamp: new Date()
      });
    } finally {
      this.loading = false;
    }
  }
}
