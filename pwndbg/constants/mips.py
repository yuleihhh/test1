from .constant import Constant

__NR_Linux = Constant('__NR_Linux',4000)
__NR_syscall = Constant('__NR_syscall',(4000 +   0))
__NR_exit = Constant('__NR_exit',(4000 +   1))
__NR_fork = Constant('__NR_fork',(4000 +   2))
__NR_read = Constant('__NR_read',(4000 +   3))
__NR_write = Constant('__NR_write',(4000 +   4))
__NR_open = Constant('__NR_open',(4000 +   5))
__NR_close = Constant('__NR_close',(4000 +   6))
__NR_waitpid = Constant('__NR_waitpid',(4000 +   7))
__NR_creat = Constant('__NR_creat',(4000 +   8))
__NR_link = Constant('__NR_link',(4000 +   9))
__NR_unlink = Constant('__NR_unlink',(4000 +  10))
__NR_execve = Constant('__NR_execve',(4000 +  11))
__NR_chdir = Constant('__NR_chdir',(4000 +  12))
__NR_time = Constant('__NR_time',(4000 +  13))
__NR_mknod = Constant('__NR_mknod',(4000 +  14))
__NR_chmod = Constant('__NR_chmod',(4000 +  15))
__NR_lchown = Constant('__NR_lchown',(4000 +  16))
__NR_break = Constant('__NR_break',(4000 +  17))
__NR_unused18 = Constant('__NR_unused18',(4000 +  18))
__NR_lseek = Constant('__NR_lseek',(4000 +  19))
__NR_getpid = Constant('__NR_getpid',(4000 +  20))
__NR_mount = Constant('__NR_mount',(4000 +  21))
__NR_umount = Constant('__NR_umount',(4000 +  22))
__NR_setuid = Constant('__NR_setuid',(4000 +  23))
__NR_getuid = Constant('__NR_getuid',(4000 +  24))
__NR_stime = Constant('__NR_stime',(4000 +  25))
__NR_ptrace = Constant('__NR_ptrace',(4000 +  26))
__NR_alarm = Constant('__NR_alarm',(4000 +  27))
__NR_unused28 = Constant('__NR_unused28',(4000 +  28))
__NR_pause = Constant('__NR_pause',(4000 +  29))
__NR_utime = Constant('__NR_utime',(4000 +  30))
__NR_stty = Constant('__NR_stty',(4000 +  31))
__NR_gtty = Constant('__NR_gtty',(4000 +  32))
__NR_access = Constant('__NR_access',(4000 +  33))
__NR_nice = Constant('__NR_nice',(4000 +  34))
__NR_ftime = Constant('__NR_ftime',(4000 +  35))
__NR_sync = Constant('__NR_sync',(4000 +  36))
__NR_kill = Constant('__NR_kill',(4000 +  37))
__NR_rename = Constant('__NR_rename',(4000 +  38))
__NR_mkdir = Constant('__NR_mkdir',(4000 +  39))
__NR_rmdir = Constant('__NR_rmdir',(4000 +  40))
__NR_dup = Constant('__NR_dup',(4000 +  41))
__NR_pipe = Constant('__NR_pipe',(4000 +  42))
__NR_times = Constant('__NR_times',(4000 +  43))
__NR_prof = Constant('__NR_prof',(4000 +  44))
__NR_brk = Constant('__NR_brk',(4000 +  45))
__NR_setgid = Constant('__NR_setgid',(4000 +  46))
__NR_getgid = Constant('__NR_getgid',(4000 +  47))
__NR_signal = Constant('__NR_signal',(4000 +  48))
__NR_geteuid = Constant('__NR_geteuid',(4000 +  49))
__NR_getegid = Constant('__NR_getegid',(4000 +  50))
__NR_acct = Constant('__NR_acct',(4000 +  51))
__NR_umount2 = Constant('__NR_umount2',(4000 +  52))
__NR_lock = Constant('__NR_lock',(4000 +  53))
__NR_ioctl = Constant('__NR_ioctl',(4000 +  54))
__NR_fcntl = Constant('__NR_fcntl',(4000 +  55))
__NR_mpx = Constant('__NR_mpx',(4000 +  56))
__NR_setpgid = Constant('__NR_setpgid',(4000 +  57))
__NR_ulimit = Constant('__NR_ulimit',(4000 +  58))
__NR_unused59 = Constant('__NR_unused59',(4000 +  59))
__NR_umask = Constant('__NR_umask',(4000 +  60))
__NR_chroot = Constant('__NR_chroot',(4000 +  61))
__NR_ustat = Constant('__NR_ustat',(4000 +  62))
__NR_dup2 = Constant('__NR_dup2',(4000 +  63))
__NR_getppid = Constant('__NR_getppid',(4000 +  64))
__NR_getpgrp = Constant('__NR_getpgrp',(4000 +  65))
__NR_setsid = Constant('__NR_setsid',(4000 +  66))
__NR_sigaction = Constant('__NR_sigaction',(4000 +  67))
__NR_sgetmask = Constant('__NR_sgetmask',(4000 +  68))
__NR_ssetmask = Constant('__NR_ssetmask',(4000 +  69))
__NR_setreuid = Constant('__NR_setreuid',(4000 +  70))
__NR_setregid = Constant('__NR_setregid',(4000 +  71))
__NR_sigsuspend = Constant('__NR_sigsuspend',(4000 +  72))
__NR_sigpending = Constant('__NR_sigpending',(4000 +  73))
__NR_sethostname = Constant('__NR_sethostname',(4000 +  74))
__NR_setrlimit = Constant('__NR_setrlimit',(4000 +  75))
__NR_getrlimit = Constant('__NR_getrlimit',(4000 +  76))
__NR_getrusage = Constant('__NR_getrusage',(4000 +  77))
__NR_gettimeofday = Constant('__NR_gettimeofday',(4000 +  78))
__NR_settimeofday = Constant('__NR_settimeofday',(4000 +  79))
__NR_getgroups = Constant('__NR_getgroups',(4000 +  80))
__NR_setgroups = Constant('__NR_setgroups',(4000 +  81))
__NR_reserved82 = Constant('__NR_reserved82',(4000 +  82))
__NR_symlink = Constant('__NR_symlink',(4000 +  83))
__NR_unused84 = Constant('__NR_unused84',(4000 +  84))
__NR_readlink = Constant('__NR_readlink',(4000 +  85))
__NR_uselib = Constant('__NR_uselib',(4000 +  86))
__NR_swapon = Constant('__NR_swapon',(4000 +  87))
__NR_reboot = Constant('__NR_reboot',(4000 +  88))
__NR_readdir = Constant('__NR_readdir',(4000 +  89))
__NR_mmap = Constant('__NR_mmap',(4000 +  90))
__NR_munmap = Constant('__NR_munmap',(4000 +  91))
__NR_truncate = Constant('__NR_truncate',(4000 +  92))
__NR_ftruncate = Constant('__NR_ftruncate',(4000 +  93))
__NR_fchmod = Constant('__NR_fchmod',(4000 +  94))
__NR_fchown = Constant('__NR_fchown',(4000 +  95))
__NR_getpriority = Constant('__NR_getpriority',(4000 +  96))
__NR_setpriority = Constant('__NR_setpriority',(4000 +  97))
__NR_profil = Constant('__NR_profil',(4000 +  98))
__NR_statfs = Constant('__NR_statfs',(4000 +  99))
__NR_fstatfs = Constant('__NR_fstatfs',(4000 + 100))
__NR_ioperm = Constant('__NR_ioperm',(4000 + 101))
__NR_socketcall = Constant('__NR_socketcall',(4000 + 102))
__NR_syslog = Constant('__NR_syslog',(4000 + 103))
__NR_setitimer = Constant('__NR_setitimer',(4000 + 104))
__NR_getitimer = Constant('__NR_getitimer',(4000 + 105))
__NR_stat = Constant('__NR_stat',(4000 + 106))
__NR_lstat = Constant('__NR_lstat',(4000 + 107))
__NR_fstat = Constant('__NR_fstat',(4000 + 108))
__NR_unused109 = Constant('__NR_unused109',(4000 + 109))
__NR_iopl = Constant('__NR_iopl',(4000 + 110))
__NR_vhangup = Constant('__NR_vhangup',(4000 + 111))
__NR_idle = Constant('__NR_idle',(4000 + 112))
__NR_vm86 = Constant('__NR_vm86',(4000 + 113))
__NR_wait4 = Constant('__NR_wait4',(4000 + 114))
__NR_swapoff = Constant('__NR_swapoff',(4000 + 115))
__NR_sysinfo = Constant('__NR_sysinfo',(4000 + 116))
__NR_ipc = Constant('__NR_ipc',(4000 + 117))
__NR_fsync = Constant('__NR_fsync',(4000 + 118))
__NR_sigreturn = Constant('__NR_sigreturn',(4000 + 119))
__NR_clone = Constant('__NR_clone',(4000 + 120))
__NR_setdomainname = Constant('__NR_setdomainname',(4000 + 121))
__NR_uname = Constant('__NR_uname',(4000 + 122))
__NR_modify_ldt = Constant('__NR_modify_ldt',(4000 + 123))
__NR_adjtimex = Constant('__NR_adjtimex',(4000 + 124))
__NR_mprotect = Constant('__NR_mprotect',(4000 + 125))
__NR_sigprocmask = Constant('__NR_sigprocmask',(4000 + 126))
__NR_create_module = Constant('__NR_create_module',(4000 + 127))
__NR_init_module = Constant('__NR_init_module',(4000 + 128))
__NR_delete_module = Constant('__NR_delete_module',(4000 + 129))
__NR_get_kernel_syms = Constant('__NR_get_kernel_syms',(4000 + 130))
__NR_quotactl = Constant('__NR_quotactl',(4000 + 131))
__NR_getpgid = Constant('__NR_getpgid',(4000 + 132))
__NR_fchdir = Constant('__NR_fchdir',(4000 + 133))
__NR_bdflush = Constant('__NR_bdflush',(4000 + 134))
__NR_sysfs = Constant('__NR_sysfs',(4000 + 135))
__NR_personality = Constant('__NR_personality',(4000 + 136))
__NR_afs_syscall = Constant('__NR_afs_syscall',(4000 + 137))
__NR_setfsuid = Constant('__NR_setfsuid',(4000 + 138))
__NR_setfsgid = Constant('__NR_setfsgid',(4000 + 139))
__NR__llseek = Constant('__NR__llseek',(4000 + 140))
__NR_getdents = Constant('__NR_getdents',(4000 + 141))
__NR__newselect = Constant('__NR__newselect',(4000 + 142))
__NR_flock = Constant('__NR_flock',(4000 + 143))
__NR_msync = Constant('__NR_msync',(4000 + 144))
__NR_readv = Constant('__NR_readv',(4000 + 145))
__NR_writev = Constant('__NR_writev',(4000 + 146))
__NR_cacheflush = Constant('__NR_cacheflush',(4000 + 147))
__NR_cachectl = Constant('__NR_cachectl',(4000 + 148))
__NR_sysmips = Constant('__NR_sysmips',(4000 + 149))
__NR_unused150 = Constant('__NR_unused150',(4000 + 150))
__NR_getsid = Constant('__NR_getsid',(4000 + 151))
__NR_fdatasync = Constant('__NR_fdatasync',(4000 + 152))
__NR__sysctl = Constant('__NR__sysctl',(4000 + 153))
__NR_mlock = Constant('__NR_mlock',(4000 + 154))
__NR_munlock = Constant('__NR_munlock',(4000 + 155))
__NR_mlockall = Constant('__NR_mlockall',(4000 + 156))
__NR_munlockall = Constant('__NR_munlockall',(4000 + 157))
__NR_sched_setparam = Constant('__NR_sched_setparam',(4000 + 158))
__NR_sched_getparam = Constant('__NR_sched_getparam',(4000 + 159))
__NR_sched_setscheduler = Constant('__NR_sched_setscheduler',(4000 + 160))
__NR_sched_getscheduler = Constant('__NR_sched_getscheduler',(4000 + 161))
__NR_sched_yield = Constant('__NR_sched_yield',(4000 + 162))
__NR_sched_get_priority_max = Constant('__NR_sched_get_priority_max',(4000 + 163))
__NR_sched_get_priority_min = Constant('__NR_sched_get_priority_min',(4000 + 164))
__NR_sched_rr_get_interval = Constant('__NR_sched_rr_get_interval',(4000 + 165))
__NR_nanosleep = Constant('__NR_nanosleep',(4000 + 166))
__NR_mremap = Constant('__NR_mremap',(4000 + 167))
__NR_accept = Constant('__NR_accept',(4000 + 168))
__NR_bind = Constant('__NR_bind',(4000 + 169))
__NR_connect = Constant('__NR_connect',(4000 + 170))
__NR_getpeername = Constant('__NR_getpeername',(4000 + 171))
__NR_getsockname = Constant('__NR_getsockname',(4000 + 172))
__NR_getsockopt = Constant('__NR_getsockopt',(4000 + 173))
__NR_listen = Constant('__NR_listen',(4000 + 174))
__NR_recv = Constant('__NR_recv',(4000 + 175))
__NR_recvfrom = Constant('__NR_recvfrom',(4000 + 176))
__NR_recvmsg = Constant('__NR_recvmsg',(4000 + 177))
__NR_send = Constant('__NR_send',(4000 + 178))
__NR_sendmsg = Constant('__NR_sendmsg',(4000 + 179))
__NR_sendto = Constant('__NR_sendto',(4000 + 180))
__NR_setsockopt = Constant('__NR_setsockopt',(4000 + 181))
__NR_shutdown = Constant('__NR_shutdown',(4000 + 182))
__NR_socket = Constant('__NR_socket',(4000 + 183))
__NR_socketpair = Constant('__NR_socketpair',(4000 + 184))
__NR_setresuid = Constant('__NR_setresuid',(4000 + 185))
__NR_getresuid = Constant('__NR_getresuid',(4000 + 186))
__NR_query_module = Constant('__NR_query_module',(4000 + 187))
__NR_poll = Constant('__NR_poll',(4000 + 188))
__NR_nfsservctl = Constant('__NR_nfsservctl',(4000 + 189))
__NR_setresgid = Constant('__NR_setresgid',(4000 + 190))
__NR_getresgid = Constant('__NR_getresgid',(4000 + 191))
__NR_prctl = Constant('__NR_prctl',(4000 + 192))
__NR_rt_sigreturn = Constant('__NR_rt_sigreturn',(4000 + 193))
__NR_rt_sigaction = Constant('__NR_rt_sigaction',(4000 + 194))
__NR_rt_sigprocmask = Constant('__NR_rt_sigprocmask',(4000 + 195))
__NR_rt_sigpending = Constant('__NR_rt_sigpending',(4000 + 196))
__NR_rt_sigtimedwait = Constant('__NR_rt_sigtimedwait',(4000 + 197))
__NR_rt_sigqueueinfo = Constant('__NR_rt_sigqueueinfo',(4000 + 198))
__NR_rt_sigsuspend = Constant('__NR_rt_sigsuspend',(4000 + 199))
__NR_pread = Constant('__NR_pread',(4000 + 200))
__NR_pwrite = Constant('__NR_pwrite',(4000 + 201))
__NR_chown = Constant('__NR_chown',(4000 + 202))
__NR_getcwd = Constant('__NR_getcwd',(4000 + 203))
__NR_capget = Constant('__NR_capget',(4000 + 204))
__NR_capset = Constant('__NR_capset',(4000 + 205))
__NR_sigaltstack = Constant('__NR_sigaltstack',(4000 + 206))
__NR_sendfile = Constant('__NR_sendfile',(4000 + 207))
__NR_getpmsg = Constant('__NR_getpmsg',(4000 + 208))
__NR_putpmsg = Constant('__NR_putpmsg',(4000 + 209))
__NR_mmap2 = Constant('__NR_mmap2',(4000 + 210))
__NR_truncate64 = Constant('__NR_truncate64',(4000 + 211))
__NR_ftruncate64 = Constant('__NR_ftruncate64',(4000 + 212))
__NR_stat64 = Constant('__NR_stat64',(4000 + 213))
__NR_lstat64 = Constant('__NR_lstat64',(4000 + 214))
__NR_fstat64 = Constant('__NR_fstat64',(4000 + 215))
__NR_pivot_root = Constant('__NR_pivot_root',(4000 + 216))
__NR_mincore = Constant('__NR_mincore',(4000 + 217))
__NR_madvise = Constant('__NR_madvise',(4000 + 218))
__NR_getdents64 = Constant('__NR_getdents64',(4000 + 219))
__NR_fcntl64 = Constant('__NR_fcntl64',(4000 + 220))
__NR_reserved221 = Constant('__NR_reserved221',(4000 + 221))
__NR_gettid = Constant('__NR_gettid',(4000 + 222))
__NR_readahead = Constant('__NR_readahead',(4000 + 223))
__NR_setxattr = Constant('__NR_setxattr',(4000 + 224))
__NR_lsetxattr = Constant('__NR_lsetxattr',(4000 + 225))
__NR_fsetxattr = Constant('__NR_fsetxattr',(4000 + 226))
__NR_getxattr = Constant('__NR_getxattr',(4000 + 227))
__NR_lgetxattr = Constant('__NR_lgetxattr',(4000 + 228))
__NR_fgetxattr = Constant('__NR_fgetxattr',(4000 + 229))
__NR_listxattr = Constant('__NR_listxattr',(4000 + 230))
__NR_llistxattr = Constant('__NR_llistxattr',(4000 + 231))
__NR_flistxattr = Constant('__NR_flistxattr',(4000 + 232))
__NR_removexattr = Constant('__NR_removexattr',(4000 + 233))
__NR_lremovexattr = Constant('__NR_lremovexattr',(4000 + 234))
__NR_fremovexattr = Constant('__NR_fremovexattr',(4000 + 235))
__NR_tkill = Constant('__NR_tkill',(4000 + 236))
__NR_sendfile64 = Constant('__NR_sendfile64',(4000 + 237))
__NR_futex = Constant('__NR_futex',(4000 + 238))
__NR_sched_setaffinity = Constant('__NR_sched_setaffinity',(4000 + 239))
__NR_sched_getaffinity = Constant('__NR_sched_getaffinity',(4000 + 240))
__NR_io_setup = Constant('__NR_io_setup',(4000 + 241))
__NR_io_destroy = Constant('__NR_io_destroy',(4000 + 242))
__NR_io_getevents = Constant('__NR_io_getevents',(4000 + 243))
__NR_io_submit = Constant('__NR_io_submit',(4000 + 244))
__NR_io_cancel = Constant('__NR_io_cancel',(4000 + 245))
__NR_exit_group = Constant('__NR_exit_group',(4000 + 246))
__NR_lookup_dcookie = Constant('__NR_lookup_dcookie',(4000 + 247))
__NR_epoll_create = Constant('__NR_epoll_create',(4000 + 248))
__NR_epoll_ctl = Constant('__NR_epoll_ctl',(4000 + 249))
__NR_epoll_wait = Constant('__NR_epoll_wait',(4000 + 250))
__NR_remap_file_pages = Constant('__NR_remap_file_pages',(4000 + 251))
__NR_set_tid_address = Constant('__NR_set_tid_address',(4000 + 252))
__NR_restart_syscall = Constant('__NR_restart_syscall',(4000 + 253))
__NR_fadvise64 = Constant('__NR_fadvise64',(4000 + 254))
__NR_statfs64 = Constant('__NR_statfs64',(4000 + 255))
__NR_fstatfs64 = Constant('__NR_fstatfs64',(4000 + 256))
__NR_timer_create = Constant('__NR_timer_create',(4000 + 257))
__NR_timer_settime = Constant('__NR_timer_settime',(4000 + 258))
__NR_timer_gettime = Constant('__NR_timer_gettime',(4000 + 259))
__NR_timer_getoverrun = Constant('__NR_timer_getoverrun',(4000 + 260))
__NR_timer_delete = Constant('__NR_timer_delete',(4000 + 261))
__NR_clock_settime = Constant('__NR_clock_settime',(4000 + 262))
__NR_clock_gettime = Constant('__NR_clock_gettime',(4000 + 263))
__NR_clock_getres = Constant('__NR_clock_getres',(4000 + 264))
__NR_clock_nanosleep = Constant('__NR_clock_nanosleep',(4000 + 265))
__NR_tgkill = Constant('__NR_tgkill',(4000 + 266))
__NR_utimes = Constant('__NR_utimes',(4000 + 267))
__NR_mbind = Constant('__NR_mbind',(4000 + 268))
__NR_get_mempolicy = Constant('__NR_get_mempolicy',(4000 + 269))
__NR_set_mempolicy = Constant('__NR_set_mempolicy',(4000 + 270))
__NR_mq_open = Constant('__NR_mq_open',(4000 + 271))
__NR_mq_unlink = Constant('__NR_mq_unlink',(4000 + 272))
__NR_mq_timedsend = Constant('__NR_mq_timedsend',(4000 + 273))
__NR_mq_timedreceive = Constant('__NR_mq_timedreceive',(4000 + 274))
__NR_mq_notify = Constant('__NR_mq_notify',(4000 + 275))
__NR_mq_getsetattr = Constant('__NR_mq_getsetattr',(4000 + 276))
__NR_vserver = Constant('__NR_vserver',(4000 + 277))
__NR_waitid = Constant('__NR_waitid',(4000 + 278))
__NR_add_key = Constant('__NR_add_key',(4000 + 280))
__NR_request_key = Constant('__NR_request_key',(4000 + 281))
__NR_keyctl = Constant('__NR_keyctl',(4000 + 282))
__NR_set_thread_area = Constant('__NR_set_thread_area',(4000 + 283))
__NR_inotify_init = Constant('__NR_inotify_init',(4000 + 284))
__NR_inotify_add_watch = Constant('__NR_inotify_add_watch',(4000 + 285))
__NR_inotify_rm_watch = Constant('__NR_inotify_rm_watch',(4000 + 286))
__NR_migrate_pages = Constant('__NR_migrate_pages',(4000 + 287))
__NR_openat = Constant('__NR_openat',(4000 + 288))
__NR_mkdirat = Constant('__NR_mkdirat',(4000 + 289))
__NR_mknodat = Constant('__NR_mknodat',(4000 + 290))
__NR_fchownat = Constant('__NR_fchownat',(4000 + 291))
__NR_futimesat = Constant('__NR_futimesat',(4000 + 292))
__NR_fstatat = Constant('__NR_fstatat',(4000 + 293))
__NR_unlinkat = Constant('__NR_unlinkat',(4000 + 294))
__NR_renameat = Constant('__NR_renameat',(4000 + 295))
__NR_linkat = Constant('__NR_linkat',(4000 + 296))
__NR_symlinkat = Constant('__NR_symlinkat',(4000 + 297))
__NR_readlinkat = Constant('__NR_readlinkat',(4000 + 298))
__NR_fchmodat = Constant('__NR_fchmodat',(4000 + 299))
__NR_faccessat = Constant('__NR_faccessat',(4000 + 300))
__NR_pselect6 = Constant('__NR_pselect6',(4000 + 301))
__NR_ppoll = Constant('__NR_ppoll',(4000 + 302))
__NR_unshare = Constant('__NR_unshare',(4000 + 303))
__NR_splice = Constant('__NR_splice',(4000 + 304))
__NR_sync_file_range = Constant('__NR_sync_file_range',(4000 + 305))
__NR_tee = Constant('__NR_tee',(4000 + 306))
__NR_vmsplice = Constant('__NR_vmsplice',(4000 + 307))
__NR_move_pages = Constant('__NR_move_pages',(4000 + 308))
__NR_set_robust_list = Constant('__NR_set_robust_list',(4000 + 272))
__NR_get_robust_list = Constant('__NR_get_robust_list',(4000 + 273))
__NR_kexec_load = Constant('__NR_kexec_load',(4000 + 274))
__NR_getcpu = Constant('__NR_getcpu',(4000 + 275))
__NR_epoll_pwait = Constant('__NR_epoll_pwait',(4000 + 276))
__NR_ioprio_set = Constant('__NR_ioprio_set',(4000 + 277))
__NR_ioprio_get = Constant('__NR_ioprio_get',(4000 + 278))
__NR_utimensat = Constant('__NR_utimensat',(4000 + 279))
__NR_signalfd = Constant('__NR_signalfd',(4000 + 280))
__NR_timerfd = Constant('__NR_timerfd',(4000 + 281))
__NR_eventfd = Constant('__NR_eventfd',(4000 + 282))
__NR_fallocate = Constant('__NR_fallocate',(4000 + 283))
__NR_timerfd_create = Constant('__NR_timerfd_create',(4000 + 284))
__NR_timerfd_gettime = Constant('__NR_timerfd_gettime',(4000 + 285))
__NR_timerfd_settime = Constant('__NR_timerfd_settime',(4000 + 286))
__SYS_NERR = Constant('__SYS_NERR',((164) + 1))
_SYS_TIME_H = Constant('_SYS_TIME_H',1)
SYS_accept = Constant('SYS_accept',(4000 + 168))
SYS_access = Constant('SYS_access',(4000 +  33))
SYS_acct = Constant('SYS_acct',(4000 +  51))
SYS_add_key = Constant('SYS_add_key',(4000 + 280))
SYS_adjtimex = Constant('SYS_adjtimex',(4000 + 124))
SYS_afs_syscall = Constant('SYS_afs_syscall',(4000 + 137))
SYS_alarm = Constant('SYS_alarm',(4000 +  27))
SYS_bdflush = Constant('SYS_bdflush',(4000 + 134))
SYS_bind = Constant('SYS_bind',(4000 + 169))
SYS_break = Constant('SYS_break',(4000 +  17))
SYS_brk = Constant('SYS_brk',(4000 +  45))
SYS_cachectl = Constant('SYS_cachectl',(4000 + 148))
SYS_cacheflush = Constant('SYS_cacheflush',(4000 + 147))
SYS_capget = Constant('SYS_capget',(4000 + 204))
SYS_capset = Constant('SYS_capset',(4000 + 205))
SYS_chdir = Constant('SYS_chdir',(4000 +  12))
SYS_chmod = Constant('SYS_chmod',(4000 +  15))
SYS_chown = Constant('SYS_chown',(4000 + 202))
SYS_chroot = Constant('SYS_chroot',(4000 +  61))
SYS_clock_getres = Constant('SYS_clock_getres',(4000 + 264))
SYS_clock_gettime = Constant('SYS_clock_gettime',(4000 + 263))
SYS_clock_nanosleep = Constant('SYS_clock_nanosleep',(4000 + 265))
SYS_clock_settime = Constant('SYS_clock_settime',(4000 + 262))
SYS_clone = Constant('SYS_clone',(4000 + 120))
SYS_close = Constant('SYS_close',(4000 +   6))
SYS_connect = Constant('SYS_connect',(4000 + 170))
SYS_creat = Constant('SYS_creat',(4000 +   8))
SYS_create_module = Constant('SYS_create_module',(4000 + 127))
SYS_delete_module = Constant('SYS_delete_module',(4000 + 129))
SYS_dup = Constant('SYS_dup',(4000 +  41))
SYS_dup2 = Constant('SYS_dup2',(4000 +  63))
SYS_epoll_create = Constant('SYS_epoll_create',(4000 + 248))
SYS_epoll_ctl = Constant('SYS_epoll_ctl',(4000 + 249))
SYS_epoll_pwait = Constant('SYS_epoll_pwait',(4000 + 276))
SYS_epoll_wait = Constant('SYS_epoll_wait',(4000 + 250))
SYS_eventfd = Constant('SYS_eventfd',(4000 + 282))
SYS_execve = Constant('SYS_execve',(4000 +  11))
SYS_exit = Constant('SYS_exit',(4000 +   1))
SYS_exit_group = Constant('SYS_exit_group',(4000 + 246))
SYS_faccessat = Constant('SYS_faccessat',(4000 + 300))
SYS_fadvise64 = Constant('SYS_fadvise64',(4000 + 254))
SYS_fallocate = Constant('SYS_fallocate',(4000 + 283))
SYS_fchdir = Constant('SYS_fchdir',(4000 + 133))
SYS_fchmod = Constant('SYS_fchmod',(4000 +  94))
SYS_fchmodat = Constant('SYS_fchmodat',(4000 + 299))
SYS_fchown = Constant('SYS_fchown',(4000 +  95))
SYS_fchownat = Constant('SYS_fchownat',(4000 + 291))
SYS_fcntl = Constant('SYS_fcntl',(4000 +  55))
SYS_fcntl64 = Constant('SYS_fcntl64',(4000 + 220))
SYS_fdatasync = Constant('SYS_fdatasync',(4000 + 152))
SYS_fgetxattr = Constant('SYS_fgetxattr',(4000 + 229))
SYS_flistxattr = Constant('SYS_flistxattr',(4000 + 232))
SYS_flock = Constant('SYS_flock',(4000 + 143))
SYS_fork = Constant('SYS_fork',(4000 +   2))
SYS_fremovexattr = Constant('SYS_fremovexattr',(4000 + 235))
SYS_fsetxattr = Constant('SYS_fsetxattr',(4000 + 226))
SYS_fstat = Constant('SYS_fstat',(4000 + 108))
SYS_fstat64 = Constant('SYS_fstat64',(4000 + 215))
SYS_fstatat = Constant('SYS_fstatat',(4000 + 293))
SYS_fstatfs = Constant('SYS_fstatfs',(4000 + 100))
SYS_fstatfs64 = Constant('SYS_fstatfs64',(4000 + 256))
SYS_fsync = Constant('SYS_fsync',(4000 + 118))
SYS_ftime = Constant('SYS_ftime',(4000 +  35))
SYS_ftruncate = Constant('SYS_ftruncate',(4000 +  93))
SYS_ftruncate64 = Constant('SYS_ftruncate64',(4000 + 212))
SYS_futex = Constant('SYS_futex',(4000 + 238))
SYS_futimesat = Constant('SYS_futimesat',(4000 + 292))
SYS_getcpu = Constant('SYS_getcpu',(4000 + 275))
SYS_getcwd = Constant('SYS_getcwd',(4000 + 203))
SYS_getdents = Constant('SYS_getdents',(4000 + 141))
SYS_getdents64 = Constant('SYS_getdents64',(4000 + 219))
SYS_getegid = Constant('SYS_getegid',(4000 +  50))
SYS_geteuid = Constant('SYS_geteuid',(4000 +  49))
SYS_getgid = Constant('SYS_getgid',(4000 +  47))
SYS_getgroups = Constant('SYS_getgroups',(4000 +  80))
SYS_getitimer = Constant('SYS_getitimer',(4000 + 105))
SYS_get_kernel_syms = Constant('SYS_get_kernel_syms',(4000 + 130))
SYS_get_mempolicy = Constant('SYS_get_mempolicy',(4000 + 269))
SYS_getpeername = Constant('SYS_getpeername',(4000 + 171))
SYS_getpgid = Constant('SYS_getpgid',(4000 + 132))
SYS_getpgrp = Constant('SYS_getpgrp',(4000 +  65))
SYS_getpid = Constant('SYS_getpid',(4000 +  20))
SYS_getpmsg = Constant('SYS_getpmsg',(4000 + 208))
SYS_getppid = Constant('SYS_getppid',(4000 +  64))
SYS_getpriority = Constant('SYS_getpriority',(4000 +  96))
SYS_getresgid = Constant('SYS_getresgid',(4000 + 191))
SYS_getresuid = Constant('SYS_getresuid',(4000 + 186))
SYS_getrlimit = Constant('SYS_getrlimit',(4000 +  76))
SYS_get_robust_list = Constant('SYS_get_robust_list',(4000 + 273))
SYS_getrusage = Constant('SYS_getrusage',(4000 +  77))
SYS_getsid = Constant('SYS_getsid',(4000 + 151))
SYS_getsockname = Constant('SYS_getsockname',(4000 + 172))
SYS_getsockopt = Constant('SYS_getsockopt',(4000 + 173))
SYS_gettid = Constant('SYS_gettid',(4000 + 222))
SYS_gettimeofday = Constant('SYS_gettimeofday',(4000 +  78))
SYS_getuid = Constant('SYS_getuid',(4000 +  24))
SYS_getxattr = Constant('SYS_getxattr',(4000 + 227))
SYS_gtty = Constant('SYS_gtty',(4000 +  32))
SYS_idle = Constant('SYS_idle',(4000 + 112))
SYS_init_module = Constant('SYS_init_module',(4000 + 128))
SYS_inotify_add_watch = Constant('SYS_inotify_add_watch',(4000 + 285))
SYS_inotify_init = Constant('SYS_inotify_init',(4000 + 284))
SYS_inotify_rm_watch = Constant('SYS_inotify_rm_watch',(4000 + 286))
SYS_io_cancel = Constant('SYS_io_cancel',(4000 + 245))
SYS_ioctl = Constant('SYS_ioctl',(4000 +  54))
SYS_io_destroy = Constant('SYS_io_destroy',(4000 + 242))
SYS_io_getevents = Constant('SYS_io_getevents',(4000 + 243))
SYS_ioperm = Constant('SYS_ioperm',(4000 + 101))
SYS_iopl = Constant('SYS_iopl',(4000 + 110))
SYS_ioprio_get = Constant('SYS_ioprio_get',(4000 + 278))
SYS_ioprio_set = Constant('SYS_ioprio_set',(4000 + 277))
SYS_io_setup = Constant('SYS_io_setup',(4000 + 241))
SYS_io_submit = Constant('SYS_io_submit',(4000 + 244))
SYS_ipc = Constant('SYS_ipc',(4000 + 117))
SYS_kexec_load = Constant('SYS_kexec_load',(4000 + 274))
SYS_keyctl = Constant('SYS_keyctl',(4000 + 282))
SYS_kill = Constant('SYS_kill',(4000 +  37))
SYS_lchown = Constant('SYS_lchown',(4000 +  16))
SYS_lgetxattr = Constant('SYS_lgetxattr',(4000 + 228))
SYS_link = Constant('SYS_link',(4000 +   9))
SYS_linkat = Constant('SYS_linkat',(4000 + 296))
SYS_Linux = Constant('SYS_Linux',4000)
SYS_listen = Constant('SYS_listen',(4000 + 174))
SYS_listxattr = Constant('SYS_listxattr',(4000 + 230))
SYS_llistxattr = Constant('SYS_llistxattr',(4000 + 231))
SYS__llseek = Constant('SYS__llseek',(4000 + 140))
SYS_lock = Constant('SYS_lock',(4000 +  53))
SYS_lookup_dcookie = Constant('SYS_lookup_dcookie',(4000 + 247))
SYS_lremovexattr = Constant('SYS_lremovexattr',(4000 + 234))
SYS_lseek = Constant('SYS_lseek',(4000 +  19))
SYS_lsetxattr = Constant('SYS_lsetxattr',(4000 + 225))
SYS_lstat = Constant('SYS_lstat',(4000 + 107))
SYS_lstat64 = Constant('SYS_lstat64',(4000 + 214))
SYS_madvise = Constant('SYS_madvise',(4000 + 218))
SYS_mbind = Constant('SYS_mbind',(4000 + 268))
SYS_migrate_pages = Constant('SYS_migrate_pages',(4000 + 287))
SYS_mincore = Constant('SYS_mincore',(4000 + 217))
SYS_mkdir = Constant('SYS_mkdir',(4000 +  39))
SYS_mkdirat = Constant('SYS_mkdirat',(4000 + 289))
SYS_mknod = Constant('SYS_mknod',(4000 +  14))
SYS_mknodat = Constant('SYS_mknodat',(4000 + 290))
SYS_mlock = Constant('SYS_mlock',(4000 + 154))
SYS_mlockall = Constant('SYS_mlockall',(4000 + 156))
SYS_mmap = Constant('SYS_mmap',(4000 +  90))
SYS_mmap2 = Constant('SYS_mmap2',(4000 + 210))
SYS_modify_ldt = Constant('SYS_modify_ldt',(4000 + 123))
SYS_mount = Constant('SYS_mount',(4000 +  21))
SYS_move_pages = Constant('SYS_move_pages',(4000 + 308))
SYS_mprotect = Constant('SYS_mprotect',(4000 + 125))
SYS_mpx = Constant('SYS_mpx',(4000 +  56))
SYS_mq_getsetattr = Constant('SYS_mq_getsetattr',(4000 + 276))
SYS_mq_notify = Constant('SYS_mq_notify',(4000 + 275))
SYS_mq_open = Constant('SYS_mq_open',(4000 + 271))
SYS_mq_timedreceive = Constant('SYS_mq_timedreceive',(4000 + 274))
SYS_mq_timedsend = Constant('SYS_mq_timedsend',(4000 + 273))
SYS_mq_unlink = Constant('SYS_mq_unlink',(4000 + 272))
SYS_mremap = Constant('SYS_mremap',(4000 + 167))
SYS_msync = Constant('SYS_msync',(4000 + 144))
SYS_munlock = Constant('SYS_munlock',(4000 + 155))
SYS_munlockall = Constant('SYS_munlockall',(4000 + 157))
SYS_munmap = Constant('SYS_munmap',(4000 +  91))
SYS_nanosleep = Constant('SYS_nanosleep',(4000 + 166))
SYS__newselect = Constant('SYS__newselect',(4000 + 142))
SYS_nfsservctl = Constant('SYS_nfsservctl',(4000 + 189))
SYS_nice = Constant('SYS_nice',(4000 +  34))
SYS_open = Constant('SYS_open',(4000 +   5))
SYS_openat = Constant('SYS_openat',(4000 + 288))
SYS_pause = Constant('SYS_pause',(4000 +  29))
SYS_personality = Constant('SYS_personality',(4000 + 136))
SYS_pipe = Constant('SYS_pipe',(4000 +  42))
SYS_pivot_root = Constant('SYS_pivot_root',(4000 + 216))
SYS_poll = Constant('SYS_poll',(4000 + 188))
SYS_ppoll = Constant('SYS_ppoll',(4000 + 302))
SYS_prctl = Constant('SYS_prctl',(4000 + 192))
SYS_pread = Constant('SYS_pread',(4000 + 200))
SYS_prof = Constant('SYS_prof',(4000 +  44))
SYS_profil = Constant('SYS_profil',(4000 +  98))
SYS_pselect6 = Constant('SYS_pselect6',(4000 + 301))
SYS_ptrace = Constant('SYS_ptrace',(4000 +  26))
SYS_putpmsg = Constant('SYS_putpmsg',(4000 + 209))
SYS_pwrite = Constant('SYS_pwrite',(4000 + 201))
SYS_query_module = Constant('SYS_query_module',(4000 + 187))
SYS_quotactl = Constant('SYS_quotactl',(4000 + 131))
SYS_read = Constant('SYS_read',(4000 +   3))
SYS_readahead = Constant('SYS_readahead',(4000 + 223))
SYS_readdir = Constant('SYS_readdir',(4000 +  89))
SYS_readlink = Constant('SYS_readlink',(4000 +  85))
SYS_readlinkat = Constant('SYS_readlinkat',(4000 + 298))
SYS_readv = Constant('SYS_readv',(4000 + 145))
SYS_reboot = Constant('SYS_reboot',(4000 +  88))
SYS_recv = Constant('SYS_recv',(4000 + 175))
SYS_recvfrom = Constant('SYS_recvfrom',(4000 + 176))
SYS_recvmsg = Constant('SYS_recvmsg',(4000 + 177))
SYS_remap_file_pages = Constant('SYS_remap_file_pages',(4000 + 251))
SYS_removexattr = Constant('SYS_removexattr',(4000 + 233))
SYS_rename = Constant('SYS_rename',(4000 +  38))
SYS_renameat = Constant('SYS_renameat',(4000 + 295))
SYS_request_key = Constant('SYS_request_key',(4000 + 281))
SYS_reserved221 = Constant('SYS_reserved221',(4000 + 221))
SYS_reserved82 = Constant('SYS_reserved82',(4000 +  82))
SYS_restart_syscall = Constant('SYS_restart_syscall',(4000 + 253))
SYS_rmdir = Constant('SYS_rmdir',(4000 +  40))
SYS_rt_sigaction = Constant('SYS_rt_sigaction',(4000 + 194))
SYS_rt_sigpending = Constant('SYS_rt_sigpending',(4000 + 196))
SYS_rt_sigprocmask = Constant('SYS_rt_sigprocmask',(4000 + 195))
SYS_rt_sigqueueinfo = Constant('SYS_rt_sigqueueinfo',(4000 + 198))
SYS_rt_sigreturn = Constant('SYS_rt_sigreturn',(4000 + 193))
SYS_rt_sigsuspend = Constant('SYS_rt_sigsuspend',(4000 + 199))
SYS_rt_sigtimedwait = Constant('SYS_rt_sigtimedwait',(4000 + 197))
SYS_sched_getaffinity = Constant('SYS_sched_getaffinity',(4000 + 240))
SYS_sched_getparam = Constant('SYS_sched_getparam',(4000 + 159))
SYS_sched_get_priority_max = Constant('SYS_sched_get_priority_max',(4000 + 163))
SYS_sched_get_priority_min = Constant('SYS_sched_get_priority_min',(4000 + 164))
SYS_sched_getscheduler = Constant('SYS_sched_getscheduler',(4000 + 161))
SYS_sched_rr_get_interval = Constant('SYS_sched_rr_get_interval',(4000 + 165))
SYS_sched_setaffinity = Constant('SYS_sched_setaffinity',(4000 + 239))
SYS_sched_setparam = Constant('SYS_sched_setparam',(4000 + 158))
SYS_sched_setscheduler = Constant('SYS_sched_setscheduler',(4000 + 160))
SYS_sched_yield = Constant('SYS_sched_yield',(4000 + 162))
SYS_send = Constant('SYS_send',(4000 + 178))
SYS_sendfile = Constant('SYS_sendfile',(4000 + 207))
SYS_sendfile64 = Constant('SYS_sendfile64',(4000 + 237))
SYS_sendmsg = Constant('SYS_sendmsg',(4000 + 179))
SYS_sendto = Constant('SYS_sendto',(4000 + 180))
SYS_setdomainname = Constant('SYS_setdomainname',(4000 + 121))
SYS_setfsgid = Constant('SYS_setfsgid',(4000 + 139))
SYS_setfsuid = Constant('SYS_setfsuid',(4000 + 138))
SYS_setgid = Constant('SYS_setgid',(4000 +  46))
SYS_setgroups = Constant('SYS_setgroups',(4000 +  81))
SYS_sethostname = Constant('SYS_sethostname',(4000 +  74))
SYS_setitimer = Constant('SYS_setitimer',(4000 + 104))
SYS_set_mempolicy = Constant('SYS_set_mempolicy',(4000 + 270))
SYS_setpgid = Constant('SYS_setpgid',(4000 +  57))
SYS_setpriority = Constant('SYS_setpriority',(4000 +  97))
SYS_setregid = Constant('SYS_setregid',(4000 +  71))
SYS_setresgid = Constant('SYS_setresgid',(4000 + 190))
SYS_setresuid = Constant('SYS_setresuid',(4000 + 185))
SYS_setreuid = Constant('SYS_setreuid',(4000 +  70))
SYS_setrlimit = Constant('SYS_setrlimit',(4000 +  75))
SYS_set_robust_list = Constant('SYS_set_robust_list',(4000 + 272))
SYS_setsid = Constant('SYS_setsid',(4000 +  66))
SYS_setsockopt = Constant('SYS_setsockopt',(4000 + 181))
SYS_set_thread_area = Constant('SYS_set_thread_area',(4000 + 283))
SYS_set_tid_address = Constant('SYS_set_tid_address',(4000 + 252))
SYS_settimeofday = Constant('SYS_settimeofday',(4000 +  79))
SYS_setuid = Constant('SYS_setuid',(4000 +  23))
SYS_setxattr = Constant('SYS_setxattr',(4000 + 224))
SYS_sgetmask = Constant('SYS_sgetmask',(4000 +  68))
SYS_shutdown = Constant('SYS_shutdown',(4000 + 182))
SYS_sigaction = Constant('SYS_sigaction',(4000 +  67))
SYS_sigaltstack = Constant('SYS_sigaltstack',(4000 + 206))
SYS_signal = Constant('SYS_signal',(4000 +  48))
SYS_signalfd = Constant('SYS_signalfd',(4000 + 280))
SYS_sigpending = Constant('SYS_sigpending',(4000 +  73))
SYS_sigprocmask = Constant('SYS_sigprocmask',(4000 + 126))
SYS_sigreturn = Constant('SYS_sigreturn',(4000 + 119))
SYS_sigsuspend = Constant('SYS_sigsuspend',(4000 +  72))
SYS_socket = Constant('SYS_socket',(4000 + 183))
SYS_socketcall = Constant('SYS_socketcall',(4000 + 102))
SYS_socketpair = Constant('SYS_socketpair',(4000 + 184))
SYS_splice = Constant('SYS_splice',(4000 + 304))
SYS_ssetmask = Constant('SYS_ssetmask',(4000 +  69))
SYS_stat = Constant('SYS_stat',(4000 + 106))
SYS_stat64 = Constant('SYS_stat64',(4000 + 213))
SYS_statfs = Constant('SYS_statfs',(4000 +  99))
SYS_statfs64 = Constant('SYS_statfs64',(4000 + 255))
SYS_stime = Constant('SYS_stime',(4000 +  25))
SYS_stty = Constant('SYS_stty',(4000 +  31))
SYS_swapoff = Constant('SYS_swapoff',(4000 + 115))
SYS_swapon = Constant('SYS_swapon',(4000 +  87))
SYS_symlink = Constant('SYS_symlink',(4000 +  83))
SYS_symlinkat = Constant('SYS_symlinkat',(4000 + 297))
SYS_sync = Constant('SYS_sync',(4000 +  36))
SYS_sync_file_range = Constant('SYS_sync_file_range',(4000 + 305))
SYS_syscall = Constant('SYS_syscall',(4000 +   0))
SYS__sysctl = Constant('SYS__sysctl',(4000 + 153))
SYS_sysfs = Constant('SYS_sysfs',(4000 + 135))
SYS_sysinfo = Constant('SYS_sysinfo',(4000 + 116))
SYS_syslog = Constant('SYS_syslog',(4000 + 103))
SYS_sysmips = Constant('SYS_sysmips',(4000 + 149))
SYS_tee = Constant('SYS_tee',(4000 + 306))
SYS_tgkill = Constant('SYS_tgkill',(4000 + 266))
SYS_time = Constant('SYS_time',(4000 +  13))
SYS_timer_create = Constant('SYS_timer_create',(4000 + 257))
SYS_timer_delete = Constant('SYS_timer_delete',(4000 + 261))
SYS_timerfd = Constant('SYS_timerfd',(4000 + 281))
SYS_timerfd_create = Constant('SYS_timerfd_create',(4000 + 284))
SYS_timerfd_gettime = Constant('SYS_timerfd_gettime',(4000 + 285))
SYS_timerfd_settime = Constant('SYS_timerfd_settime',(4000 + 286))
SYS_timer_getoverrun = Constant('SYS_timer_getoverrun',(4000 + 260))
SYS_timer_gettime = Constant('SYS_timer_gettime',(4000 + 259))
SYS_timer_settime = Constant('SYS_timer_settime',(4000 + 258))
SYS_times = Constant('SYS_times',(4000 +  43))
SYS_tkill = Constant('SYS_tkill',(4000 + 236))
SYS_truncate = Constant('SYS_truncate',(4000 +  92))
SYS_truncate64 = Constant('SYS_truncate64',(4000 + 211))
SYS_ulimit = Constant('SYS_ulimit',(4000 +  58))
SYS_umask = Constant('SYS_umask',(4000 +  60))
SYS_umount = Constant('SYS_umount',(4000 +  22))
SYS_umount2 = Constant('SYS_umount2',(4000 +  52))
SYS_uname = Constant('SYS_uname',(4000 + 122))
SYS_unlink = Constant('SYS_unlink',(4000 +  10))
SYS_unlinkat = Constant('SYS_unlinkat',(4000 + 294))
SYS_unshare = Constant('SYS_unshare',(4000 + 303))
SYS_unused109 = Constant('SYS_unused109',(4000 + 109))
SYS_unused150 = Constant('SYS_unused150',(4000 + 150))
SYS_unused18 = Constant('SYS_unused18',(4000 +  18))
SYS_unused28 = Constant('SYS_unused28',(4000 +  28))
SYS_unused59 = Constant('SYS_unused59',(4000 +  59))
SYS_unused84 = Constant('SYS_unused84',(4000 +  84))
SYS_uselib = Constant('SYS_uselib',(4000 +  86))
SYS_ustat = Constant('SYS_ustat',(4000 +  62))
SYS_utime = Constant('SYS_utime',(4000 +  30))
SYS_utimensat = Constant('SYS_utimensat',(4000 + 279))
SYS_utimes = Constant('SYS_utimes',(4000 + 267))
SYS_vhangup = Constant('SYS_vhangup',(4000 + 111))
SYS_vm86 = Constant('SYS_vm86',(4000 + 113))
SYS_vmsplice = Constant('SYS_vmsplice',(4000 + 307))
SYS_vserver = Constant('SYS_vserver',(4000 + 277))
SYS_wait4 = Constant('SYS_wait4',(4000 + 114))
SYS_waitid = Constant('SYS_waitid',(4000 + 278))
SYS_waitpid = Constant('SYS_waitpid',(4000 +   7))
SYS_write = Constant('SYS_write',(4000 +   4))
SYS_writev = Constant('SYS_writev',(4000 + 146))
