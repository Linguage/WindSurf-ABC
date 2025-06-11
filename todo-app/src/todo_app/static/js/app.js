// DOM 元素
const taskForm = document.getElementById('task-form');
const taskInput = document.getElementById('task-input');
const deadlineInput = document.getElementById('deadline-input');
const taskList = document.getElementById('task-list');
const filterButtons = document.querySelectorAll('.filter-btn');

// 当前筛选器
let currentFilter = 'all';

// 初始化应用
document.addEventListener('DOMContentLoaded', () => {
    loadTasks();
    setupEventListeners();
});

// 设置事件监听器
function setupEventListeners() {
    // 添加任务
    taskForm.addEventListener('submit', handleAddTask);
    
    // 筛选按钮
    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            filterButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
            currentFilter = button.dataset.filter;
            loadTasks();
        });
    });
}

// 加载任务
async function loadTasks() {
    try {
        const response = await fetch('/api/tasks');
        let tasks = await response.json();
        
        // 应用筛选
        tasks = tasks.filter(task => {
            if (currentFilter === 'active') return !task.completed;
            if (currentFilter === 'completed') return task.completed;
            return true; // all
        });
        
        renderTasks(tasks);
    } catch (error) {
        console.error('加载任务失败:', error);
    }
}

// 渲染任务列表
function renderTasks(tasks) {
    taskList.innerHTML = '';
    
    tasks.forEach(task => {
        const taskElement = document.createElement('li');
        taskElement.className = 'task-item';
        if (task.completed) {
            taskElement.classList.add('completed');
        }
        
        // 计算倒计时文本
        const countdownText = getCountdownText(task);
        
        taskElement.innerHTML = `
            <input type="checkbox" class="task-checkbox" ${task.completed ? 'checked' : ''} data-id="${task.id}">
            <div class="task-content">
                <span class="task-title">${escapeHtml(task.title)}</span>
                <span class="task-deadline">
                    截止时间: ${new Date(task.deadline).toLocaleString()}
                    <span class="countdown ${getCountdownClass(task)}">${countdownText}</span>
                </span>
            </div>
            <div class="task-actions">
                <button class="edit-btn" data-id="${task.id}">编辑</button>
                <button class="delete-btn" data-id="${task.id}">删除</button>
            </div>
        `;
        
        // 添加事件监听器
        const checkbox = taskElement.querySelector('.task-checkbox');
        const editBtn = taskElement.querySelector('.edit-btn');
        const deleteBtn = taskElement.querySelector('.delete-btn');
        
        checkbox.addEventListener('change', () => toggleTaskCompletion(task.id, checkbox.checked));
        editBtn.addEventListener('click', () => editTask(task));
        deleteBtn.addEventListener('click', () => deleteTask(task.id));
        
        taskList.appendChild(taskElement);
    });
    
    // 更新倒计时
    startCountdownTimer();
}

// 添加新任务
async function handleAddTask(e) {
    e.preventDefault();
    
    const title = taskInput.value.trim();
    const deadline = deadlineInput.value;
    
    if (!title || !deadline) return;
    
    try {
        const response = await fetch('/api/tasks', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                title,
                deadline: new Date(deadline).toISOString()
            })
        });
        
        if (response.ok) {
            taskInput.value = '';
            deadlineInput.value = '';
            loadTasks();
        }
    } catch (error) {
        console.error('添加任务失败:', error);
    }
}

// 切换任务完成状态
async function toggleTaskCompletion(taskId, completed) {
    try {
        await fetch(`/api/tasks/${taskId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ completed })
        });
        
        loadTasks();
    } catch (error) {
        console.error('更新任务状态失败:', error);
    }
}

// 编辑任务
function editTask(task) {
    const newTitle = prompt('编辑任务:', task.title);
    if (newTitle === null) return;
    
    const newDeadline = prompt('编辑截止时间 (YYYY-MM-DD HH:MM):', 
        new Date(task.deadline).toISOString().slice(0, 16));
    
    if (newTitle !== null && newDeadline !== null) {
        updateTask(task.id, {
            title: newTitle,
            deadline: newDeadline
        });
    }
}

// 更新任务
async function updateTask(taskId, updates) {
    try {
        await fetch(`/api/tasks/${taskId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(updates)
        });
        
        loadTasks();
    } catch (error) {
        console.error('更新任务失败:', error);
    }
}

// 删除任务
async function deleteTask(taskId) {
    if (!confirm('确定要删除这个任务吗？')) return;
    
    try {
        await fetch(`/api/tasks/${taskId}`, {
            method: 'DELETE'
        });
        
        loadTasks();
    } catch (error) {
        console.error('删除任务失败:', error);
    }
}

// 获取倒计时文本
function getCountdownText(task) {
    if (task.completed) return '已完成';
    
    const now = new Date();
    const deadline = new Date(task.deadline);
    const diff = deadline - now;
    
    if (diff <= 0) return '已过期';
    
    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    
    if (days >= 1) return `剩余${days}天`;
    if (hours >= 1) return `剩余${hours}小时`;
    if (minutes >= 1) return `剩余${minutes}分钟`;
    return '即将到期';
}

// 获取倒计时样式类
function getCountdownClass(task) {
    if (task.completed) return 'completed';
    
    const now = new Date();
    const deadline = new Date(task.deadline);
    const diff = deadline - now;
    
    if (diff <= 0) return 'urgent';
    if (diff < 60 * 60 * 1000) return 'urgent'; // 小于1小时
    return '';
}

// 启动倒计时定时器
function startCountdownTimer() {
    // 每分钟更新一次倒计时
    setInterval(() => {
        const countdowns = document.querySelectorAll('.countdown');
        countdowns.forEach(countdown => {
            const taskItem = countdown.closest('.task-item');
            const taskId = taskItem.querySelector('.task-checkbox').dataset.id;
            const isCompleted = taskItem.querySelector('.task-checkbox').checked;
            const deadline = new Date(taskItem.querySelector('.task-deadline').textContent.replace('截止时间: ', ''));
            
            const task = {
                id: taskId,
                completed: isCompleted,
                deadline: deadline.toISOString()
            };
            
            countdown.textContent = getCountdownText(task);
            
            // 更新样式类
            countdown.className = 'countdown ' + getCountdownClass(task);
        });
    }, 60000);
}

// 转义HTML特殊字符
function escapeHtml(unsafe) {
    return unsafe
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}
